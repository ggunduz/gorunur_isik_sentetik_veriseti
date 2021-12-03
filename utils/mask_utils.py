import pycocotools._mask as _mask

iou         = _mask.iou
merge       = _mask.merge
frPyObjects = _mask.frPyObjects

def encode(bimask):
    if len(bimask.shape) == 3:
        return _mask.encode(bimask)
    elif len(bimask.shape) == 2:
        h, w = bimask.shape
        return _mask.encode(bimask.reshape((h, w, 1), order='F'))[0]

def decode(rleObjs):
    if type(rleObjs) == list:
        return _mask.decode(rleObjs)
    else:
        return _mask.decode([rleObjs])[:,:,0]

def area(rleObjs):
    if type(rleObjs) == list:
        return _mask.area(rleObjs)
    else:
        return _mask.area([rleObjs])[0]

def toBbox(rleObjs):
    if type(rleObjs) == list:
        return _mask.toBbox(rleObjs)
    else:
        return _mask.toBbox([rleObjs])[0]
    
def annToRLE(ann, 
             h,
             w,):
        """
        Convert annotation which can be polygons, uncompressed RLE to RLE.
        :return: binary mask (numpy 2D array)
        """
        segm = ann['segmentation']
        if type(segm) == list:
            # polygon -- a single object might consist of multiple parts
            # we merge all parts into one mask rle code
            rles = frPyObjects(segm, h, w)
            rle = merge(rles)
        elif type(segm['counts']) == list:
            # uncompressed RLE
            rle = frPyObjects(segm, h, w)
        else:
            # rle
            rle = ann['segmentation']
        return rle

def annToMask(ann,
             h, 
             w,):
    """
    Convert annotation which can be polygons, uncompressed RLE, or RLE to binary mask.
    :return: binary mask (numpy 2D array)
    """
    rle = annToRLE(ann,
             h,
             w,)
    m = decode(rle)
    return m