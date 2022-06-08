from django.test import TestCase
from .models import Comment, Image, Like, User

# Create your tests here.

class commentTestClass(TestCase):
    def setUp(self):
        self.comment = Comment(comm= 'comment1')
        self.comment.save_comment()   
        self.user = User(user= "vicky")
        self.image = Image(user= "nice")
        self.image.save_image()
        self.coment = Comment(image = self.image, comment =self.comment,user= self.user )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.coment, Comment))
    
    def test_save_method(self):
        self.coment.save_comment()
        commes = Comment.objects.all()
        self.assertTrue(len(commes) > 0)
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.comment1 = Comment(comm= 'hello')
        self.comment1.save_comment()
        self.nairobi = User(location_name= 'nairobi')
        self.image1 = Image(user= "vic",comment= self.comment1 ,caption ="vics", pub_date= "2/2/2222", )
    def test_instance(self):
        self.assertTrue(isinstance(self.image1 , Image))
        
    def test_save_method(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
class LikeTestClass(TestCase):
    def setUp(self): 
        self.user = User(user= "vicky")
        self.image.save()
        self.image = Image(image= "nice")
        self.image.save_image()
        self.liky = Like(image = self.image, user =self.user, pub_date ='3/3/3333' )
    def test_instance(self):
        self.assertTrue(isinstance(self.liky, Like))
        
    def test_save_method(self):
        self.liky.save_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes) > 0)