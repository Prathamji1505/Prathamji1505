# Profile verification

Recorded on 7 November 2026 for the initial profile overview.

## Rendered checks

The README was rendered using GitHub's Markdown API, then previewed in the actual public profile DOM before publication. Both themes were inspected; the identity graphics stay dark while native text follows GitHub's viewer theme.

| Viewport width | README image | Document overflow | Broken README images |
| --- | --- | --- | --- |
| 1440 px | Desktop, 1600 × 580 | None | 0 |
| 768 px | Desktop, 1600 × 580 | None | 0 |
| 390 px | Mobile, 800 × 900 | None | 0 |
| 360 px | Mobile, 800 × 900 | None | 0 |

All three navigation destinations returned HTTP 200. The Activity target uses the inspected `js-contribution-activity` anchor. Keyboard Tab moves between the native links, with GitHub's visible solid 2 px focus outline.

## Assets and source

- Both PNGs match the intended master dimensions and carry embedded origin metadata.
- Both outlined SVG masters passed checks for external resources, scripts, event handlers, and foreign objects.
- The README references existing local images, and `git diff --check` passed.
- The font source is pinned; the original SIL OFL notice is retained.
- The design detector reported no findings for the changed targets. Its scope is mechanical checks, not a guarantee of design quality.
- A separate finish review inspected all five theme/viewport captures and both raster masters and returned **ship**, with no material fixes.

This is a static profile-document review. It does not establish application behavior, project performance, or user adoption. Project showcases and skill claims were deliberately excluded at the owner's request.
