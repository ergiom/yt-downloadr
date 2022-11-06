'''
    Classes
    -------
    IndexRoute
        application index route
'''

from flask import render_template

class IndexRoute:
    '''
        Class representing / route

        Methods
        -------
        get
            flask return for / http get
    '''

    def get(self):
        '''flask return for / http get'''
        return render_template('index.html')
