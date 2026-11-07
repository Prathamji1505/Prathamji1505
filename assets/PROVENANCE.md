# Profile identity assets

Created on 7 November 2026 for Pratham Sengar / Prathamji1505.

The user requested a dark palette matching his existing sepia cat-with-sunglasses GitHub avatar. That photograph was inspected for visual direction. It remains unchanged and is not redistributed in these assets.

The sunglasses motif is an original flat geometric construction in `tools/build_assets.py`. SVG masters contain outlined lettering and vector paths, with no scripts, external resources, animation, embedded fonts, or product screenshots.

The two PNGs are browser rasterizations of the corresponding SVG masters. The README uses PNG for consistent rendering, with a dedicated portrait composition selected by `picture` on narrow screens. These are identity graphics, not product or project evidence.

## Typography

Bricolage Grotesque is used under the SIL Open Font License. The original notice is in [licenses/BricolageGrotesque-OFL.txt](licenses/BricolageGrotesque-OFL.txt). Weight, width, and optical size are instantiated before lettering is outlined. Viewing the assets requires no font download.

Pinned source: [Google Fonts, revision 6ce172f](https://github.com/google/fonts/blob/6ce172f74aa355ea43eb964fa4a91570a4d3064d/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz%2Cwdth%2Cwght%5D.ttf).

## Rebuilding

Download that font to `.local/fonts/BricolageGrotesque.ttf`, then run:

```sh
python -m pip install --target .local/lib -r tools/requirements.txt
python tools/build_assets.py
```

The script builds both SVG masters and a hash manifest. Rasterize each SVG in a browser at its exact viewBox size: 1600 × 580 and 800 × 900. Save a lossless PNG of the entire viewport with no browser UI, resizing, or clipping. Preserve the SVG origin in PNG metadata and record the output hashes in the manifest. Update identity wording in the generator and personal prose in README.md.
