import numpy as np
import cv2

def x_cord_contour(contour):
    
    M = cv2.moments(contour)
    return (int(M['m10']/M['m00']))


def makeSquare(not_square):
    
    BLACK = [0,0,0]
    
    img_dim = not_square.shape
    height = img_dim[0]
    width = img_dim[1]
    
    if (height == width):
        
        square = not_square
        return square
    else:
        doublesize = cv2.resize(not_square,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
        
        height = height * 2
        width = width * 2
        
        if (height > width):
            pad = int((height - width)/2)
            
            doublesize_square = cv2.copyMakeBorder(doublesize,0,0,pad,pad,cv2.BORDER_CONSTANT,value=BLACK)
        else:
            pad = (width - height)/2
            
            doublesize_square = cv2.copyMakeBorder(doublesize,pad,pad,0,0,\
                                                   cv2.BORDER_CONSTANT,value=BLACK)
            
    doublesize_square_dim = doublesize_square.shape
    return doublesize_square


def resize_to_pixel(dimensions, image):
    
    buffer_pix = 4
    dimensions  = dimensions - buffer_pix
    squared = image
    
    r = float(dimensions) / squared.shape[1]
    dim = (dimensions, int(squared.shape[0] * r))
    
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
    img_dim2 = resized.shape
    height_r = img_dim2[0]
    width_r = img_dim2[1]
    
    BLACK = [0,0,0]
    
    if (height_r > width_r):
        
        resized = cv2.copyMakeBorder(resized,0,0,0,1,cv2.BORDER_CONSTANT,value=BLACK)
        
    if (height_r < width_r):
        
        resized = cv2.copyMakeBorder(resized,1,0,0,0,cv2.BORDER_CONSTANT,value=BLACK)
    p = 2
    ReSizedImg = cv2.copyMakeBorder(resized,p,p,p,p,cv2.BORDER_CONSTANT,value=BLACK)
    img_dim = ReSizedImg.shape
    
    height = img_dim[0]
    width = img_dim[1]
    
    return ReSizedImg
