from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlistApp.api.views import movie_list, movie_details
from watchlistApp.api.views import WatchListAv, WatchDetailAV, StreamPlatformAv,StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate ,StreamPlatformVS, UserReview

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/',WatchListAv.as_view() , name='watch-list' ),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='watch-details'),
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAv.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('reviews/', UserReview.as_view(), name='user-review-detail'),
]
