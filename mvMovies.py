import glob
import shutil


def mvMovies():
    for f in (glob.glob('/Users/levin/Downloads/**/*.mkv') +
              glob.glob('/Users/levin/Downloads/**/*.rmvb') +
              glob.glob('/Users/levin/Downloads/**/*.mp4')):
        shutil.move(f, '/Users/levin/Documents/movies')
