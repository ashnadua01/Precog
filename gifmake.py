import imageio
images = []
filenames = ['/Users/ashnadua/Downloads/pendingCases2010.png', '/Users/ashnadua/Downloads/pendingCases2011.png', '/Users/ashnadua/Downloads/pendingCases2012.png', '/Users/ashnadua/Downloads/pendingCases2013.png', '/Users/ashnadua/Downloads/pendingCases2014.png', '/Users/ashnadua/Downloads/pendingCases2015.png', '/Users/ashnadua/Downloads/pendingCases2016.png', '/Users/ashnadua/Downloads/pendingCases2017.png', '/Users/ashnadua/Downloads/pendingCases2018.png']
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('/Users/ashnadua/desktop/pendingCases.gif', images)