'''The `contact_sheet` function creates a contact sheet which is a PIL.Image.Image object with multiple images in sequence.
   
   Parameters
    ----------
    ipath : str
    The 'ipath' parameter is the image path (URL or local path) pointing directly to the image.
    numimages: numeric
    The 'numimages' parameter refers to the number of images the user wants on the contact sheet.
    sheet_mode: str
    This refers to the form of the contact sheet. In 'long' mode means height > width; 'wide' mode means width > height; 'balanced' means width = height.
    ncols: numeric
    The number of columns used when the sheet_mode is balanced.
    
    Returns
    -------
    PIL.Image.Image
        The function `contact_sheet` returns a PIL.Image.Image object.
        Chande Momentum Oscillator (CMO) values added.
        
    Notes
    -----
    An adopted function from Christopher Brooks from the University of Michigan.
    Part of the UMich Python specialization.
    
    References:
    1. https://www.coursera.org/learn/python-project/lecture/gDshw/additional-pil-functions
    Examples
    --------
    ```{python}

    masseff = "C://Users//GrandProf//Pictures//mass.effect//me1.png"
    
    # Example - Get a contact sheet
      contact_sheet(masseff,numimages = 10, sheet_mode = 'long', ncols = 2)
'''

def contact_sheet(ipath, numimages, sheet_mode, ncols=None):
  from PIL import ImageEnhance
  from PIL import Image
  import math
  
  with Image.open(ipath).convert('RGB') as img:
    img.load()
  
  #get image properties
  imw = img.width
  imh = img.height
  
  #PIL.ImageEnhance.Brightness object
  enhancer = ImageEnhance.Brightness(img)
  
  #get the template image
  images = []
  for i in range(0, numimages):
    images.append(enhancer.enhance(i/numimages))
  template_image = images[0]
  
  if sheet_mode == 'long':
    contact_sheet = Image.new(template_image.mode, (template_image.width, numimages*template_image.height) )
    curr_y = 0
    for image in images[1:]:
      contact_sheet.paste(image, (0, curr_y) ) #xy
      curr_y = curr_y + imh
    contact_sheet = contact_sheet.resize( (int(imh/3),int(imw)) )
    contact_sheet.show()
    
  elif sheet_mode == 'wide':
    contact_sheet = Image.new(template_image.mode, (numimages*template_image.width, template_image.height) )
    curr_x = 0
    for image in images[1:]:
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
    for image in images[1:]:
      contact_sheet.paste(image, (curr_x, curr_y) )
      if curr_x + template_image.width == contact_sheet.width:
        curr_x = 0
        curr_y = curr_y + template_image.height
      else:
        curr_x = curr_x + template_image.width
        
    contact_sheet = contact_sheet.resize((int(contact_sheet.width/ncols),int(contact_sheet.height/nrows)))
    contact_sheet.show()
    
masseff = os.getenv('mass_effect')

cs = contact_sheet(ipath = masseff,numimages = 10, sheet_mode = 'balanced', ncols=3)

