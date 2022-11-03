'''
    Classes
    -------
    BasicInfo
        dataclass holding basic info about video
'''
from dataclasses import dataclass

@dataclass
class BasicInfo:
    '''
        Dataclass holding basic info about video

        Attributes
        ----------
        link: str
            link to the video

        title: str
            video title

        formats: dict[
                    format_id: {
                        'extension': str,
                        'resolution': str,
                        'size': str
                    }
                ]
            dictionary of available formats
    '''
    link: str
    title: str
    formats: dict
