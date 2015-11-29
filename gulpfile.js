/**
 * Some sweet gulp action,
 * 'cause who doesn't like burgers
 * and shakes together, yeah?
 */

// Include dependancies
var
    gulp = require('gulp'),
    sass = require('gulp-ruby-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cmq = require('gulp-combine-media-queries')
;

// Define static assets
var
    root = 'static/',
    assets = {
        styles: root + '/styles/'
    }
;

// Styles
gulp.task('styles', function(){
    return sass('static/styles/sass/',{
        style: 'compressed',
        noCache: true
    })
    .pipe(autoprefixer({
        browsers: ['last 2 versions']
    }))
    .pipe(cmq({
        log: true
    }))
    .pipe(gulp.dest('static/styles/'));
});

// Watch
gulp.task('watch',function(){
    gulp.watch('static/styles/sass/**/*.scss',['styles']);
});

// Default
gulp.task('default', [
    'styles',
    'watch'
]);
