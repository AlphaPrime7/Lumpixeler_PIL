'''The `pixelmod` function creates a PIL.Image.Image object with modified pixels.
   
   Parameters
    ----------
    img : str
    A string representing an image.
    
    channel: numeric
    The channel number. The class within the function has the definitions.
    
    lum: numeric
    The intensity value used in pixel manipulation.
    
    image_mode: str
    A string 'RGB' or 'RGBA' used to determine the use of the alpha channel in 
    pixel manipulation. This parameter is also part of the 'lumpixeler' function.
    
    Returns
    -------
    PIL.Image.Image
        The function `pixelmod` returns a PIL.Image object with modified pixels.
        
    Notes
    -----
    The best part of learning how to manipulate pixels at a higher-level meaning withoug seeing 
    actual coordinates using numpy.
    
    References:
    1. https://www.coursera.org/learn/python-project/lecture/gDshw/additional-pil-functions
    Examples
    --------
    ```{python}
    
    # Example - Pixel extraction and manipulation.
      pixelmod(img, channel=1, lum=0.5, image_mode='RGBA')
'''

def pixelmod(img, channel, lum, image_mode = None):
  import PIL
  
  from PIL import Image
  from PIL import ImageDraw
  from enum import Enum
  
  class ChannelCode(Enum):
    red = 0
    green = 1
    blue = 2
    alpha = 3
    
  width, height = img.size
    
  blank_image = Image.new(img.mode, (width, height))
  
  for row in range(height): #img.size[1]
    for col in range(width): #img.size[0]
      
      p = img.getpixel( (col, row) )
      
      if channel == ChannelCode.red.value:
        if image_mode == 'RGBA':
          blank_image.putpixel( (col, row), ( int(p[0]*lum), p[1], p[2], int(p[3]*lum)  ))
        else:
          blank_image.putpixel( (col, row), ( int(p[0]*lum), p[1], p[2] ))
        
      elif channel == ChannelCode.green.value:
        if image_mode == 'RGBA':
          blank_image.putpixel( (col, row), (p[0], int(p[1]*lum), p[2], int(p[3]*lum) ))
        else:
          blank_image.putpixel( (col, row), (p[0], int(p[1]*lum), p[2] ))
          
      elif channel == ChannelCode.blue.value:
        if image_mode == 'RGBA':
          blank_image.putpixel( (col, row), (p[0], p[1], int(p[2]*lum), int(p[3]*lum) ))
        else:
          blank_image.putpixel( (col, row), (p[0], p[1], int(p[2]*lum) ))
        
  return(blank_image)

'''The `rendertext` renders text to a PIL object..
   
    Parameters
    ----------
    image : str
    A string for the image of interest.
    
    channel: numeric
    The channel number. The class within the function has the definitions.
    
    lum: numeric
    The intensity value used in pixel manipulation.
    
    font_num: numeric
    A number representing the font family. Also used in the parent function. 
    A limited number of choices are given.
    
    Returns
    -------
    PIL.Image.Image
        The function `rendertext` returns a PIL object with rendered text.
        
    Notes
    -----
    A cool function to help render text to images for labeling purposes.  Think of this 
    as a way of adding labels to images just as is done for a data frame.
    
    References:
    1. https://www.coursera.org/learn/python-project/lecture/gDshw/additional-pil-functions
    Examples
    --------
    ```{python}
    
    # Example - Get a contact sheet
      rendertext(image, channel=1, lum=0.6, font_num=2)
'''

def rendertext(image, channel, lum, font_num):
  
  import PIL
  from PIL import Image
  
  from PIL import ImageDraw
  from PIL import ImageFont
  from urllib.request import urlopen
  
  from enum import Enum
  
  class FontCode(Enum):
    fanwood = 1
    emotional = 2
    free = 3
    courier = 4
    
  width, height = image.size
  
  if font_num == FontCode.fanwood.value:
    text = "channel {} lum {}".format(channel, lum)
    font_url = 'https://github.com/AlphaPrime7/pilfonts/blob/main/fanwood/Fanwood-Italic.otf?raw=true'
    #font = ImageFont.FreeTypeFont(font=r"fanwood\Fanwood-Italic.otf", size=50)
    font = ImageFont.FreeTypeFont(font=urlopen(font_url), size=130)
    text_draw_obj = ImageDraw.Draw(image)
    text_draw_obj.text( ( int(width/2), (height - 100) ), text, fill='white',font=font, align='left' )  
  
  elif font_num == FontCode.emotional.value:
    text = "channel {} lum {}".format(channel, lum)
    font_url = 'https://github.com/AlphaPrime7/pilfonts/blob/main/emotional-rescue-font/EmotionalRescue.ttf?raw=true'
    font = ImageFont.truetype(font=urlopen(font_url), size=130)
    text_draw_obj = ImageDraw.Draw(image)
    text_draw_obj.text( ( int(width/2), (height - 100) ), text, fill='white',font=font, align='left' )  
  
  elif font_num == FontCode.free.value:
    text = "channel {} lum {}".format(channel, lum)
    font_url = 'https://github.com/AlphaPrime7/pilfonts/blob/main/feelfree-font/FeelfreePersonalUse.ttf?raw=true'
    font = ImageFont.truetype(font=urlopen(font_url), size=130)
    text_draw_obj = ImageDraw.Draw(image)
    text_draw_obj.text( ( int(width/2), (height - 100) ), text, fill='white',font=font, align='left' )  
    
  elif font_num == FontCode.courier.value:
    text = "channel {} lum {}".format(channel, lum)
    font_url = 'https://github.com/AlphaPrime7/pilfonts/blob/main/courier-prime-code/courier-prime-code-italic.ttf?raw=true'
    font = ImageFont.truetype(font=urlopen(font_url), size=130)
    text_draw_obj = ImageDraw.Draw(image)
    text_draw_obj.text( ( int(width/2), (height - 100) ), text, fill='white',font=font, align='left' )  

'''The `lumpixeler` function creates a contact sheet which is a PIL.Image.Image object with images with difference luminescence.
   
   Parameters
    ----------
    ipath : str
    The 'ipath' parameter is the image path (URL or local path) pointing directly to the image.
    
    lums: tuple
    The 'lums' parameter is a tuple of intensity or luminescence values.
    
    sheet_mode: str
    This refers to the form of the contact sheet. In 'long' mode means height > width; 
    'wide' mode means width > height; 'balanced' means width = height.
    
    image_mode: str
    A string either "RGB" or "RGBA". Essentially limiting this function to these image modes.
    
    font_num: numeric
    A parameter that allows the program to choose amongs a selection of fonts to use.
    
    ncols: numeric
    The number of columns used when the sheet_mode is balanced.
    
    Returns
    -------
    PIL.Image.Image
        The function `lumpixeler` returns a PIL.Image.Image object.
        
    Notes
    -----
    A great learning function that finally teaches me pixel manipulation and image data structures.
    
    References:
    1. https://www.coursera.org/learn/python-project/lecture/gDshw/additional-pil-functions
    Examples
    --------
    ```{python}

    masseff = "C://Users//GrandProf//Pictures//mass.effect//me1.png"
    
    # Example - Get images with different luminescence
      lums = [0.1,0.5,0.9]
      lumpixeler(ipath, lums = lums, image_mode = 'RGB', sheet_mode = 'balanced', font_num=1, ncols = 2)
'''

def lumpixeler(ipath, lums, sheet_mode, image_mode = None, font_num = None, ncols=None):
  import PIL
  from PIL import Image
  from PIL import ImageDraw
  import math
  import time #CPU exec time
  import timeit #code execution time
  from datetime import datetime
  
  
  start = timeit.default_timer()
  start_adv = datetime.now()
  st = time.process_time()
  
  if image_mode == 'RGB' or image_mode is None:
    with Image.open(ipath).convert('RGB') as img:
      img.load()
  else:
    with Image.open(ipath) as img:
      img.load()
    
  channels = [0,1,2]
    
  if font_num is None:
    font_num = 1
      
  width, height = img.size
  
  image_with_text = Image.new(img.mode, (width, (height+100) ) )
  image_with_text.paste(img, (0,0))
  
  imw, imh = image_with_text.size
  
  images = []

  for channel in channels:
    for lum in lums:
      images.append(pixelmod(image_with_text, channel, lum, image_mode = image_mode))
      rendertext(images[-1], channel, lum, font_num=font_num)
      
  numimages = len(images)
  
  if sheet_mode == 'long':
    canvas = Image.new(img.mode, (image_with_text.width, numimages*image_with_text.height) )
    curr_y = 0
    for image in images:
      canvas.paste(image, (0, curr_y) ) #xy
      curr_y = curr_y + imh
    canvas = canvas.resize( (int(imh/3),int(imw)) )
    canvas.show()
    
  elif sheet_mode == 'wide':
    canvas = Image.new(img.mode, (numimages*image_with_text.width, image_with_text.height) )
    curr_x = 0
    for image in images:
      canvas.paste(image, (curr_x, 0) )
      curr_x = curr_x + imw
    canvas = canvas.resize(( int(imh),int(imw/3) ))
    canvas.show()
    
  elif sheet_mode == 'balanced' and numimages > 2:
    if ncols is None:
      ncols = 1
    nrows = math.ceil(len(images)/ncols)
    canvas = Image.new(img.mode, (ncols*image_with_text.width, nrows*image_with_text.height) )
    curr_x = 0
    curr_y = 0
    for image in images:
      canvas.paste(image, (curr_x, curr_y) )
      if curr_x + image_with_text.width == canvas.width:
        curr_x = 0
        curr_y = curr_y + image_with_text.height
      else:
        curr_x = curr_x + image_with_text.width
        
    canvas = canvas.resize((int(canvas.width/ncols),int(canvas.height/nrows)))
    canvas.show()
    
  stop = timeit.default_timer()
  stop_adv = datetime.now()
  et = time.process_time()
  
  td = (stop_adv - start_adv).total_seconds()
  res_secs = (et - st)
  res_min = (et - st) / 60
  
  print('Time (seconds): ', stop - start) 
  print(f"Execution time for cross-validation is: {td:.03f}s")
  print('CPU Execution time:', res_secs, 'seconds')
  print('CPU Execution time:', res_min, 'minutes')

masseff = os.getenv('mass_effect')

#CPU exec time at 153 seconds or ~2.5 minutes
#stopwatch recording on iphone indicated about ~2.34 compared to 2.35 for CPU time.
lumpixeler(ipath = masseff, lums = (0.1,0.5,0.9), sheet_mode = 'balanced', image_mode = 'RGB', font_num = 1, ncols=3)
lumpixeler(ipath = masseff, lums = (0.1,0.5,0.9), sheet_mode = 'balanced', image_mode = 'RGBA', font_num = 3, ncols=3)

