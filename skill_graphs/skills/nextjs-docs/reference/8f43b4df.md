## Use minimal nesting[](https://nextjs.org/docs/pages/api-reference/components/head#use-minimal-nesting)
`title`, `meta` or any other elements (e.g. `script`) need to be contained as **direct** children of the `Head` element, or wrapped into maximum one level of `<React.Fragment>` or arrays—otherwise the tags won't be correctly picked up on client-side navigations.
