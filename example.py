from Fotocrib import *

#create the client and thumbnail the image
client = Fotocrib("http://fotocrib.com/images/bentley.jpg", "bentley_thumbnail.jpg")
client.thumbnail()


#change source image and filename and label
client.imgSrc = "http://fotocrib.com/images/gal.jpg"
client.filename = "gal_label.jpg"
client.label("GALLARDO", "Center")


#round corners
client.imgSrc = "http://fotocrib.com/images/bwaterfall.jpg"
client.filename = "waterfall_round.jpg"
client.roundCorners(56)


#round frame
client.imgSrc = "http://fotocrib.com/images/monet.jpg"
client.filename = "monet_roundFrame.jpg"
client.roundFrame(12, 44, 100, 223, 11)


#oil paint
client.imgSrc = "http://fotocrib.com/images/tdot.jpg"
client.filename = "tdot_paint.jpg"
client.paint()



