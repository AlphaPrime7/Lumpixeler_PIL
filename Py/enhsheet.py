'''The `enhsheet` function creates a contact sheet which is a PIL.Image.Image object with multiple images that have varying parameters.
   
   Parameters
    ----------
    ipath : str
    The 'ipath' parameter is the image path (URL or local path) pointing directly to the image.
    numimages: numeric
    The 'numimages' parameter refers to the number of images the user wants on the contact sheet.
    enh_scale: numeric
    The 'enh_scale' parameter determines image brightness. A lower value leads to peak brightness.
    sheet_mode: str
    This refers to the form of the contact sheet. In 'long' mode means height > width; 'wide' mode means width > height; 'balanced' means width = height.
    ncols: numeric
    The number of columns used when the sheet_mode is balanced.
    enh_type: str
    A string for the enhancement feature. Has 4 features.
    
    Returns
    -------
    PIL.Image.Image
        The function `enhsheet` returns a PIL.Image.Image object.
        
    Notes
    -----
    A function created with code adaptations from Christopher Brooks from the University of Michigan.
    Part of the UMich Python specialization.
    
    References:
    1. https://www.coursera.org/learn/python-project/lecture/gDshw/additional-pil-functions
    
    Examples
    --------
    ```{python}
    
    masseff = os.getenv('mass_effect')
    
    # Example - Get a contact sheet
      enhsheet(masseff,numimages = 10, enh_scale = 5, sheet_mode = 'long', ncols = 2, enh_type= None)
      enhsheet(ipath = masseff,numimages = 16, enh_scale = 5, sheet_mode = 'balanced', ncols=3, enh_type= 'contrast')
   ```
'''

def enhsheet(ipath, numimages, enh_scale, sheet_mode, ncols=None, enh_type= None):
  from PIL import ImageEnhance
  from PIL import Image
  import math
  
  with Image.open(ipath).convert('RGB') as img:
    img.load()
  
  #get image properties
  imw = img.width
  imh = img.height
  
  enhancer = ImageEnhance.Brightness(img)

  #PIL.ImageEnhance.Brightness object
  if enh_type == 'brightness' or type is None:
    enhancer = ImageEnhance.Brightness(img)
  elif enh_type == 'contrast':
    enhancer = ImageEnhance.Contrast(img)
  elif enh_type == 'color':
    enhancer = ImageEnhance.Color(img)
  elif enh_type == 'sharpness':
    enhancer = ImageEnhance.Sharpness(img)
  
  #get the template image
  images = []
  for i in range(0, numimages):
    images.append(enhancer.enhance(i/enh_scale))
  template_image = images[0]

  images = images[1:]
  
  if sheet_mode == 'long':
    contact_sheet = Image.new(template_image.mode, (template_image.width, numimages*template_image.height) )
    curr_y = 0
    for image in images:
      contact_sheet.paste(image, (0, curr_y) ) #xy
      curr_y = curr_y + imh
    contact_sheet = contact_sheet.resize( (int(imh/3),int(imw)) )
    contact_sheet.show()
    
  elif sheet_mode == 'wide':
    contact_sheet = Image.new(template_image.mode, (numimages*template_image.width, template_image.height) )
    curr_x = 0
    for image in images:
      contact_sheet.paste(image, (curr_x, 0) )
      curr_x = curr_x + imw
    contact_sheet = contact_sheet.resize(( int(imh),int(imw/3) ))
    contact_sheet.show()
    
  elif sheet_mode == 'balanced' and numimages > 2:
    if ncols is None:
      ncols = 1
    nrows = math.ceil(len(images[1:])/ncols)
    contact_sheet = Image.new(template_image.mode, (ncols*template_image.width, nrows*template_image.height) )
    curr_x = 0
    curr_y = 0
    for image in images:
      contact_sheet.paste(image, (curr_x, curr_y) )
      if curr_x + template_image.width == contact_sheet.width:
        curr_x = 0
        curr_y = curr_y + template_image.height
      else:
        curr_x = curr_x + template_image.width
        
    contact_sheet = contact_sheet.resize((int(contact_sheet.width/ncols),int(contact_sheet.height/nrows)))
    contact_sheet.show()
    
masseff = os.getenv('mass_effect')

enhsheet(ipath = masseff,numimages = 16, enh_scale = 3, sheet_mode = 'balanced', ncols=3, enh_type= "contrast")

