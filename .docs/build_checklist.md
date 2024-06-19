# Build checklist
**Pre commit**
- [ ] Update version in `/src/modules/core/metadata`
- [ ] Execute `npm run build-static`
  - [ ] Run `npm run build-auto` if changes to user vars have been made.

**Commit**
- [ ] Commit `/src/modules/core/metadata` only
- [ ] Commit message is `Bump version > 1.10.*`

**Actions**
- [ ] Run make-release

**Release**
- [ ] Correct tag version
- [ ] Correct version in title
- [ ] Example release body:
```
**Full Changelog**: https://github.com/TakosThings/Fluent-Discord/compare/v1.10.8...v1.10.9

## Highlights
* 
```
- [ ] Ensure version numbers to compare are correct
- [ ] Contributors to merged PRs are credited
- [ ] CSS files are uploaded

**Issues**
- [ ] Close issues resolved in this release
