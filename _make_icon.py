"""Generate REPS app icons.

Design: a sunrise over a horizon with water ripples, on a cream
rounded square. The four Avatar elements: sun=fire, horizon=earth,
ripples=water, sky gradient=air. Read as "morning practice / daily
cycle" which is what the app is about.

Run: python _make_icon.py
"""
from PIL import Image, ImageDraw

# Palette (matches REPS Air theme + multi-element accents)
BG = (244, 239, 227, 255)        # cream
SKY = (127, 169, 201)             # accent sky blue (Air)
SUN = (232, 155, 95)              # warm monk orange (Fire)
HORIZON = (107, 142, 85)          # sage green (Earth)
WATER = (58, 123, 140)            # deep teal (Water)


def quad_bezier_points(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def make_icon(size: int) -> Image.Image:
    # Render at 4x for crisp edges, then downsample.
    scale = 4
    s = size * scale
    img = Image.new("RGBA", (s, s), BG)
    d = ImageDraw.Draw(img, "RGBA")

    # Sky gradient — soft blue at top fading to cream by mid-height.
    sky = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sky)
    grad_h = int(s * 0.55)
    for i in range(grad_h):
        a = int(75 * (1 - i / grad_h))
        sd.rectangle((0, i, s, i + 1), fill=(*SKY, a))
    img = Image.alpha_composite(img, sky)
    d = ImageDraw.Draw(img, "RGBA")

    # Sun — solid disc just above the horizon.
    sun_r = int(s * 0.17)
    sun_cx, sun_cy = s // 2, int(s * 0.50)
    d.ellipse(
        (sun_cx - sun_r, sun_cy - sun_r, sun_cx + sun_r, sun_cy + sun_r),
        fill=(*SUN, 255),
    )

    # Subtle warm halo around the sun.
    halo = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    hd = ImageDraw.Draw(halo)
    for r_off, alpha in [(int(s * 0.04), 40), (int(s * 0.08), 22), (int(s * 0.13), 10)]:
        hd.ellipse(
            (sun_cx - sun_r - r_off, sun_cy - sun_r - r_off,
             sun_cx + sun_r + r_off, sun_cy + sun_r + r_off),
            fill=(*SUN, alpha),
        )
    img = Image.alpha_composite(halo, img)
    d = ImageDraw.Draw(img, "RGBA")

    # Horizon — gentle curve, sage green.
    thickness = max(6, int(s * 0.025))
    horizon_pts = quad_bezier_points(
        (int(s * 0.10), int(s * 0.65)),
        (int(s * 0.50), int(s * 0.60)),
        (int(s * 0.90), int(s * 0.65)),
    )
    d.line(horizon_pts, fill=(*HORIZON, 255), width=thickness, joint="curve")

    # Two water ripples below horizon — receding teal arcs.
    for y_pct, alpha, t_factor in [(0.74, 210, 0.020), (0.83, 150, 0.016)]:
        rip_pts = quad_bezier_points(
            (int(s * 0.20), int(s * y_pct)),
            (int(s * 0.50), int(s * (y_pct + 0.015))),
            (int(s * 0.80), int(s * y_pct)),
        )
        d.line(
            rip_pts,
            fill=(*WATER, alpha),
            width=max(4, int(s * t_factor)),
            joint="curve",
        )

    # Round the corners with a mask.
    radius = int(s * 0.22)
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, s, s), radius=radius, fill=255)
    img.putalpha(mask)

    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    import os
    out_dir = os.path.dirname(os.path.abspath(__file__))
    for sz in (192, 512):
        path = os.path.join(out_dir, f"icon-{sz}.png")
        make_icon(sz).save(path, optimize=True)
        print(f"wrote {path}")
