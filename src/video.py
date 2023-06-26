from src.channel import Channel
import os, json


class Video:
    """Класс Video"""
    def __init__(self, video_id: str) -> None:
        self.__video_id = video_id
        self.video_response = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                  id=self.__video_id).execute()
        try:
            self.video_link = 'http://youtube.com/watch?v=' + self.__video_id
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']
        except IndexError:
            self.video_link = None
            self.title: str = None
            self.view_count: int = None
            self.like_count: int = None
            self.comment_count: int = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    """Класс PLVideo"""
    def __init__(self, video_id, video_pl_id):
        super().__init__(video_id)
        self.__video_pl_id = video_pl_id
        self.playlist_videos = Channel.get_service().playlistItems().list(playlistId=self.__video_pl_id,
                                                                          part='contentDetails',
                                                                          maxResults=50, ).execute()
