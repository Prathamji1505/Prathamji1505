---
name: Pratham Sengar Profile
description: A mysterious charcoal and sepia identity featuring the exact existing avatar cat.
colors:
  ground: "#191514"
  field: "#352923"
  ivory: "#F4ECE4"
  sand: "#C7AE9C"
  quiet: "#B59C8C"
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

The profile presents the exact cat photograph from Pratham's existing avatar in a mysterious, restrained charcoal and deep sepia frame. Broad ivory-and-sand lettering introduces the person. The source photograph and GitHub avatar remain unchanged; a standalone eyewear symbol is not the personal identity.

GitHub owns native typography, navigation, focus behavior, and the viewer's page theme. This design system governs the static masthead graphics only.

## Colors

The five normative colors are in the frontmatter. Charcoal is the canvas, deep sepia frames the portrait, ivory carries the first name and supporting copy, sand distinguishes the surname, and quiet taupe carries the handle. The photograph retains its original colors and grain.

**The Avatar Identity Rule.** Use the actual source photo at the owner's request. Preserve its pose, expression, fur, existing accessories, and photographic pixels. Mystery comes from the dark framing and restrained composition.

## Typography

Bricolage Grotesque is instantiated at weights 700 and 450, width 100, optical size 72, then exported as filled outlines. The seven size roles in the frontmatter remain source-artboard dimensions. Viewing the finished PNGs requires no fonts. Native README prose follows GitHub's own typography.

**The Outlined Identity Rule.** Preserve the pinned font axes and outlined lettering across both compositions.

## Layout

The desktop canvas remains 1600 × 580 with the sepia field beginning at x=1045. The photo fits a 478 × 400 box at x=1084, y=28 using contain scaling. Its full square crop remains visible, with a status line below at baseline 490.

The portrait canvas remains 800 × 900. Name baselines are 177 and 315. The sepia band spans y=386 through 704; the full photo fits a 400 × 300 box at x=200, y=395. Tagline and handle remain below. The README selects this dedicated portrait composition through 600 viewport pixels inclusive.

## Elevation & Depth

Solid dark fields frame the naturally shaded source photograph. No glow, simulated depth, or added photographic effects are applied. GitHub's native surfaces are outside this system.

## Shapes

The artboard, portrait crop, and supporting fields have square corners. Preserve the source photograph's entire crop rather than approximating the cat with vector shapes or masks.

## Components

The wide and portrait mastheads ship as assets/profile-cat-desktop.png and assets/profile-cat-mobile.png. The actual source portrait is assets/cat-portrait.png. Generated SVG layout intermediates live under ignored .local/masters/ and resolve the local photo, keeping duplicated image bytes out of the public source.

The two mastheads are static. Their text, links, and image alternative text remain readable in native Markdown. No custom JavaScript, buttons, or animation are introduced. The sidecar previews point to the exact published masthead PNGs.

## Do's and Don'ts

- Keep the real avatar cat recognizable and its photo pixels unchanged.
- Keep charcoal, deep sepia, warm lettering, and generous clear space.
- Use the dedicated portrait composition on small screens.
- Keep prose and navigation native to GitHub.
- Preserve image origin metadata and the font notice.
- A standalone glasses mark and a newly invented replacement cat are outside the owner's chosen identity.
