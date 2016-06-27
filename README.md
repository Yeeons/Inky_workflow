# Inky_workflow
Foundation Inky workflow

Introduction
A work flow for adding in sections to a eDM. Uses the foundation ZURB Stack.

How it works
Once you have install your Zurb stack and modified your gulp file to look like:
'''
function pages() {
  return gulp.src('src/pages/**/*.html')
    .pipe(panini({
      root: 'src/pages',
      layouts: 'src/layouts',
      partials: 'src/partials',
      helpers: 'src/helpers',
      data: 'src/data'
    }))
    .pipe(inky())
    .pipe(gulp.dest('dist'));
}
'''

You run the python file with in the project. This will ask for the name of the new section and a headline and body copy.
After this it'll create a json file to put the content in, a html file with panini handles in witch to pull the json data from and then modifiy the orginal default file to add in the new section.

Todo
Better section placement.
Multipule body parts.
