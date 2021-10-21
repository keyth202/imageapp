from flask import (Blueprint, render_template, request, flash, redirect,url_for)
from .imagewalk import imageWalk

views = Blueprint('views', __name__)

@views.route('/')
def home():
    imgList = imageWalk()
    return render_template('home.html',filepath =imgList[0], imgList = imgList)


@views.route('/register')
def register():
   
    return render_template('register.html')

