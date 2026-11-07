---
name: Pratham Sengar Profile
description: A warm, dark personal identity anchored by an original sunglasses mark.
colors:
  ground: "#191514"
  field: "#73574A"
  ivory: "#F4ECE4"
  sand: "#C7AE9C"
  quiet: "#B59C8C"
  lens: "#151211"
  reflection: "#A07C65"
typography:
  display-desktop:
    fontFamily: "Bricolage Grotesque"
    fontSize: "171px"
    fontWeight: 700
    letterSpacing: "-2px"
    fontVariation: "'wght' 700, 'wdth' 100, 'opsz' 72"
  display-mobile:
    fontFamily: "Bricolage Grotesque"
    fontSize: "143px"
    fontWeight: 700
    letterSpacing: "-1.5px"
    fontVariation: "'wght' 700, 'wdth' 100, 'opsz' 72"
  tagline-desktop:
    fontFamily: "Bricolage Grotesque"
    fontSize: "42px"
    fontWeight: 450
    letterSpacing: "0px"
    fontVariation: "'wght' 450, 'wdth' 100, 'opsz' 72"
  tagline-mobile:
    fontFamily: "Bricolage Grotesque"
    fontSize: "44px"
    fontWeight: 450
    letterSpacing: "0px"
    fontVariation: "'wght' 450, 'wdth' 100, 'opsz' 72"
  handle-desktop:
    fontFamily: "Bricolage Grotesque"
    fontSize: "25px"
    fontWeight: 450
    letterSpacing: "0px"
    fontVariation: "'wght' 450, 'wdth' 100, 'opsz' 72"
  handle-mobile:
    fontFamily: "Bricolage Grotesque"
    fontSize: "27px"
    fontWeight: 450
    letterSpacing: "0px"
    fontVariation: "'wght' 450, 'wdth' 100, 'opsz' 72"
  status-desktop:
    fontFamily: "Bricolage Grotesque"
    fontSize: "32px"
    fontWeight: 450
    letterSpacing: "0px"
    fontVariation: "'wght' 450, 'wdth' 100, 'opsz' 72"
components:
  masthead-desktop:
    backgroundColor: "{colors.ground}"
    width: "1600px"
    height: "580px"
  masthead-mobile:
    backgroundColor: "{colors.ground}"
    width: "800px"
    height: "900px"
---

# Design System: Pratham Sengar Profile

## Overview

**Creative North Star: "Dark personal note"**

A warm charcoal and sepia identity borrows the tonal character of Pratham's existing sunglasses-cat avatar. Broad, closely set lettering introduces the person, while a flat geometric sunglasses mark supplies the recognizable detail. The avatar itself remains unchanged.

This system governs the authored identity graphics. GitHub owns the surrounding page, native README typography, link and keyboard-focus treatment, and the viewer's theme. A dark graphic therefore has to remain readable when the surrounding GitHub page is light. The graphic carries personality; the native document carries readable prose and real navigation.

**Key Characteristics:**

- Warm dark fields with ivory, sand, and quiet secondary lettering.
- Outlined Bricolage Grotesque lettering with a strong two-line name.
- Original sunglasses geometry with restrained reflection strokes.
- Separate wide and portrait compositions, each rendered as a static asset.
- Native GitHub reading and navigation behavior.

## Colors

The palette is brown rather than blue-black, with warm light lettering and a subdued sepia field. The frontmatter is the normative palette extracted from `tools/build_assets.py` and `assets/manifest.json`.

### Primary

- **Warm Sepia Field** (`field`): the right-hand desktop field and central mobile band behind the sunglasses.
- **Muted Copper Reflection** (`reflection`): the two small curved strokes that distinguish the lens surfaces without simulating gloss.

### Neutral

- **Charcoal Brown** (`ground`): the complete identity canvas underneath all other artwork.
- **Warm Ivory** (`ivory`): the first name, tagline, and desktop status line.
- **Soft Sand** (`sand`): the surname; this color change separates the two name lines without changing type weight.
- **Quiet Taupe** (`quiet`): the account handle, subordinate to the name and tagline.
- **Near-black Lens** (`lens`): the solid sunglasses silhouette and temple strokes.

### Named Rules

**The Avatar Kinship Rule.** Preserve the warm sepia and charcoal relationship established by the unchanged avatar; let the original geometric mark carry the connection.

The sidecar's tonal ramps are synthesized inspection swatches. They do not expand the approved shipping palette.

## Typography

**Identity Font:** Bricolage Grotesque, instantiated before export and converted to filled vector outlines. No runtime font or fallback is required to view the shipped graphics.

**Body Font:** GitHub-owned native README typography; this repository does not prescribe its family, size, or spacing.

**Character:** Heavy, broad name lettering provides the signature. Medium-weight sentence-case copy softens it and keeps the supporting information calm. “Outlined” describes the export format, not hollow or stroked lettering.

### Hierarchy

- **Display:** the uppercase first name and surname use the two display tokens. Both lines share weight and size within each composition; ivory and sand distinguish them.
- **Tagline:** the sentence-case “Curious by default.” uses the corresponding tagline token.
- **Handle:** the account name uses the smaller, quiet-colored handle token.
- **Status:** the wide composition alone uses `status-desktop` for “Currently building.”

Token sizes and tracking describe pixels in the source artboard, not CSS sizes for native README text. The graphics scale proportionally with their available width. The source places glyphs at explicit baselines; it defines no browser line-height scale.

### Named Rules

**The Outlined Identity Rule.** Instantiate the pinned font axes and export lettering as vector paths so every viewer receives the same identity without a font download.

## Layout

The wide master uses the dimensions in `masthead-desktop`. Its sepia field begins at horizontal coordinate 1045 and occupies the remaining 555 artboard pixels. The two name baselines sit at 225 and 390 with a shared left coordinate of 64; supporting copy begins near that same optical edge. The sunglasses occupy the right field, leaving clear space around both name and mark.

The portrait master uses the dimensions in `masthead-mobile`. It stacks the two name lines above a full-width sepia band, then places the tagline and handle below it. The band begins at vertical coordinate 386 and is 318 artboard pixels tall. The name baselines are 177 and 315 with a shared left coordinate of 42. This is a separate composition, not a crop of the wide graphic.

README's `picture` selects the portrait asset at viewport widths through 600 pixels, inclusive, and the wide asset above that boundary. Both images retain their full aspect ratio and scale down to the available document width. The graphic has no shared UI spacing scale; its coordinates are composition-specific. GitHub determines the prose column, native heading rhythm, and page gutters.

## Elevation & Depth

The identity is flat: solid fields, filled lettering, a solid sunglasses silhouette, and two reflection strokes. There are no shadows, gradients, bevels, textured overlays, or animated depth effects. The graphic's layers are distinguished by color and silhouette. GitHub's own page surfaces are outside this system's scope.

## Shapes

The identity canvas and sepia field have square corners and no border. The sunglasses combine curved lens contours with a narrow bridge and rounded temple strokes. Within the unscaled mark, the reflection strokes have width 3 and the temple strokes have width 12, both with rounded caps. The mark is scaled uniformly for each composition. These curves belong to the illustration; they do not establish a rounded-card or button system.

## Components

### Wide identity masthead

A static, name-led introduction with the sunglasses placed to the right. The authored component is `assets/profile-desktop.svg`; `assets/profile-desktop.png` is the matching shipping raster. The two-field composition, outlined lettering, and original mark form one graphic. It has no hover, focus, active, loading, or disabled state.

### Portrait identity masthead

A static, stacked interpretation using `assets/profile-mobile.svg` and its matching PNG. It retains the name, mark, tagline, and handle while omitting the wide graphic's secondary status line. Native README prose retains the current-work information. Responsive selection is performed by `picture`, with the wide image as fallback.

### Native document and navigation

Headings, paragraphs, value statements, and real GitHub links remain native markup. The image has descriptive alternative text; its SVG masters also include a title and description. GitHub provides link appearance and interaction states. No custom button, card, input, chip, navigation widget, or JavaScript component exists to inherit from this identity.

The sidecar contains the actual wide and portrait SVGs as self-contained component previews. It adds no invented UI primitives or interactive states.

## Do's and Don'ts

### Do:

- **Do** retain the warm sepia and charcoal relationship of the existing avatar.
- **Do** preserve the two-tone name, original sunglasses geometry, and clear space around them.
- **Do** instantiate Bricolage Grotesque and export lettering as vector paths before creating the matching lossless raster.
- **Do** use the dedicated portrait composition at the existing responsive boundary.
- **Do** keep readable prose and real navigation in native GitHub markup with descriptive image alternative text.

### Don't:

- **Don't** replace the avatar or trace its photograph into the identity artwork.
- **Don't** substitute a font-dependent rasterization or hollow-stroke treatment for the shipped filled lettering.
- **Don't** crop the wide master to stand in for the portrait composition.
- **Don't** treat graphic typography tokens as overrides for GitHub's native body, links, focus treatment, or viewer theme.
- **Don't** promote synthesized tonal-ramp swatches into shipping colors without an intentional design change.
