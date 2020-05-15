from PIL import Image
import array as arr
import math
import copy

### Parent Class MyList and its Iterator ###
class MyListIterator:
    ''' Iterator class to make MyList iterable.
    https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
    '''

    def __init__(self, lst):
        # MyList object reference
        self._lst: MyList = lst
        # member variable to keep track of current index
        self._index: int = 0

    def __next__(self):
        ''''Returns the next value from the stored MyList instance.'''
        if self._index < len(self._lst):
            value = self._lst[self._index]
            self._index += 1
            return value
        # End of Iteration
        raise StopIteration


class MyList:
    '''A list interface.'''

    def __init__(self, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.

        The list is static. It only has space for size elements.

        Args:
        - size: size of the list; space is reserved for these many elements. 
        - value: the optional initial value of the created elements.

        Returns:
        none
        """
        self.size = size

    def __len__(self) -> int:
        '''Returns the size of the list. Allows len() to be called on it.

        Ref: https://stackoverflow.com/q/7642434/1382487

        Args:

        Returns:
        the size of the list.
        '''
        pass

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.

        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        pass

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.

        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Setting invalid list index {i} in list of size {self.size()}'
        pass

    def __iter__(self) -> MyListIterator:
        '''Returns an iterator that allows iteration over this list.

        Ref: https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/

        Args:

        Returns:
        an iterator that allows iteration over this list.
        '''
        return MyListIterator(self)

    def get(self, i: int):
        '''Returns the value at index, i.

        Alternate to use of indexing syntax.

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''
        return self[i]

    def set(self, i: int, value) -> None:
        '''Sets the element at index, i, to value.

        Alternate to use of indexing syntax.

        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''
        self[i] = value


"*****************************************************************************************************"
### ArrayList using python array module ###

class ArrayList(MyList):
    def __init__(self, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.

        The list is static. It only has space for size elements.

        Args:
        - size: size of the list; space is reserved for these many elements. 
        - value: the optional initial value of the created elements.

        Returns:
        none
        """
        #Arraylist size saved
        self.size = size
        # Array initialized
        lst = []
        for i in range(0, size):
            for j in range(len(value)):
                lst.append(value[j])
        self.lst = arr.array('i', lst)

    def __len__(self) -> int:
        '''Returns the size of the list. Allows len() to be called on it.

        Ref: https://stackoverflow.com/q/7642434/1382487

        Args:

        Returns:
        the size of the list.
        '''
        return (self.size)

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.

        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''
        # Ensure bounds.
        assert 0 <= i < len(self.lst),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        return ((self.lst[i*3], self.lst[(i*3)+1], self.lst[(i*3)+2]))

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.

        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''
        # Ensure bounds.
        assert 0 <= i < len(self.lst),\
            f'Setting invalid list index {i} in list of size {self.size()}'
        self.lst[(i*3)] = value[0]
        self.lst[(i*3)+1] = value[1]
        self.lst[(i*3)+2] = value[2]


"*****************************************************************************************************"
### PointerList using singlely link list ###

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class PointerList(MyList):
    '''A list interface'''

    def __init__(self, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.

        The list is static. It only has space for size elements.

        Args:
        - size: size of the list; space is reserved for these many elements. 
        - value: the optional initial value of the created elements.

        Returns:
        none
        """
        self.size = size
        self.header = Node(value)
        temp = self.header
        for i in range(0, size):
            temp.next = Node(value)
            temp = temp.next

    def __len__(self) -> int:
        '''Returns the size of the list. Allows len() to be called on it.

        Ref: https://stackoverflow.com/q/7642434/1382487

        Args:

        Returns:
        the size of the list.
        '''
        return self.size

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.

        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        temp = self.header
        for i in range(1, i):
            if temp.next != None:
                temp = temp.next
        return (temp.data)

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.

        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Setting invalid list index {i} in list of size {self.size()}'
        temp = self.header
        for i in range(1, i):
            if temp.next != None:
                temp = temp.next
        temp.data = value



"*****************************************************************************************************"
### MyImage Class ###

class MyImage:
    """ Holds a flattened RGB image and its dimensions.
    """

    def __init__(self, size: (int, int), pointer = False) -> None:
        """Initializes a black image of the given size.

        Args:
        - size: (width, height) specifies the dimensions to create.

        Returns:
        none
        """
        # Save size, create a list of the desired size with black pixels.
        width, height = self.size = size
        self.pointer = pointer
        if pointer == True:
            self.pixels: PointerList = PointerList(width * height, value=(0, 0, 0))
        else:
            self.pixels: ArrayList = ArrayList(width * height, value=(0 , 0, 0))
        # ^ CHANGE this line to use your implementation of MyList.

    def _get_index(self, r: int, c: int) -> int:
        """Returns the list index for the given row, column coordinates.

        This is an internal function for use in class methods only. It should
        not be used or called from outside the class.

        Args:
        - r: the row coordinate
        - c: the column coordinate

        Returns:
        the list index corresponding to the given row and column coordinates
        """
        # Confirm bounds, compute and return list index.
        width, height = self.size
        assert 0 <= r < height and 0 <= c < width, "Bad image coordinates: "\
            f"(r, c): ({r}, {c}) for image of size: {self.size}"
        return r*width + c

    def open(path: str, pointer = False) :
        """Creates and returns an image containing from the information at file path.

        The image format is inferred from the file name. The read image is
        converted to RGB as our type only stores RGB.

        Args:
        - path: path to the file containing image information

        Returns:
        the image created using the information from file path.
        """
        # Use PIL to read the image information and store it in our instance.
        img: PIL.Image = Image.open(path)
        myimg: MyImage = MyImage(img.size, pointer)
        width, height = img.size
        # Covert image to RGB. https://stackoverflow.com/a/11064935/1382487
        img: PIL.Image = img.convert('RGB')
        # Get list of pixel values (https://stackoverflow.com/a/1109747/1382487),
        # copy to our instance and return it.
        for i, rgb in enumerate(list(img.getdata())):
            myimg.pixels.set(i, rgb)
        return myimg

    def save(self, path: str) -> None:
        """Saves the image to the given file path.

        The image format is inferred from the file name.

        Args:
        - path: the image has to be saved here.

        Returns:
        none
        """
        # Use PIL to write the image.
        img: PIL.Image = Image.new("RGB", self.size)
        img.putdata([rgb for rgb in self.pixels])
        img.save(path)

    def get(self, r: int, c: int) -> (int, int, int):
        """Returns the value of the pixel at the given row and column coordinates.

        Args:
        - r: the row coordinate
        - c: the column coordinate

        Returns:
        the stored RGB value of the pixel at the given row and column coordinates.
        """
        return self.pixels[self._get_index(r, c)]

    def set(self, r: int, c: int, rgb: (int, int, int)) -> None:
        """Write the rgb value at the pixel at the given row and column coordinates.

        Args:
        - r: the row coordinate
        - c: the column coordinate
        - rgb: the rgb value to write

        Returns:
        none
        """
        self.pixels[self._get_index(r, c)] = rgb

    def show(self) -> None:
        """Display the image in a GUI window.

        Args:

        Returns:
        none
        """
        # Use PIL to display the image.
        img: PIL.Image = Image.new("RGB", self.size)
        img.putdata([rgb for rgb in self.pixels])
        img.show()


"*****************************************************************************************************"
### Image Operations ###

def remove_channel(src: MyImage, red: bool = False, green: bool = False,
                   blue: bool = False) -> MyImage:
    """Returns a copy of src in which the indicated channels are suppressed.

    Suppresses the red channel if no channel is indicated. src is not modified.

    Args:
    - src: the image whose copy the indicated channels have to be suppressed.
    - red: suppress the red channel if this is True.
    - green: suppress the green channel if this is True.
    - blue: suppress the blue channel if this is True.

    Returns:
    a copy of src with the indicated channels suppressed.
    """
    new_image = copy.copy(src)
    # Saving the list size to iterate
    length = new_image.size[0] * new_image.size[1]
    for i in range(0, length):
        if green == True:
            new_image.pixels[i] = (new_image.pixels[i][0], 0, new_image.pixels[i][2])
        if blue == True:
            new_image.pixels[i] = (new_image.pixels[i][0], new_image.pixels[i][1], 0)
        if red == True:
            new_image.pixels[i] = (0, new_image.pixels[i][1], new_image.pixels[i][2])
        if blue == False and green == False:
            new_image.pixels[i] = (0, new_image.pixels[i][1], new_image.pixels[i][2])
    return new_image

# Rotation function for square images only
def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.

    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image whose rotations have to be stored and returned.

    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    new_image = MyImage((2*src.size[0], 2*src.size[1]), src.pointer)
    # vertical = width and horizontal = height 
    width = new_image.size[0]
    height = new_image.size[1]
    for i in range(width):
        for j in range(height):
            # top left portion
            if i < width//2 and j < height//2:
                value = src.get(j, (width//2) - 1 - i)
                new_image.set(i, j, value)
            # top right portion
            elif i < width//2 and j >= height//2:
                value = src.get(i, j - (height//2))
                new_image.set(i, j, value)
            # bottom left portion
            elif i >= width//2 and j < height//2:
                value = src.get(width - 1 - i, (height//2) - 1 - j)
                new_image.set(i, j, value)
            # bottom right portion
            elif i >= width//2 and j >= height//2:
                value = src.get(height - 1 - j,  i - (width//2))
                new_image.set(i, j, value)
                    
    return (new_image)
    

# helper functions for masking
def file_read(maskfile : str):
    mask = open(maskfile, 'r')
    file_lst = list(mask.read())
    loop = int(file_lst.pop(0))
    file_lst.pop(0)
    n = 0
    lst = []
    for i in range(loop):
        lst.append([])
    
    for i in range(0, loop):
        for j in range(0, loop):
                lst[i].append(int(file_lst[n]))
                n += 2
    mask.close()
    return lst


def value_mask(src: MyImage, maskfile: str, average: bool = True):
    """Returns an copy of src with the mask from maskfile applied to it.

    maskfile specifies a text file which contains an n by n mask. It has the
    following format:
    - the first line contains n
    - the next n^2 lines contain 1 element each of the flattened mask

    Args:
    - src: the image on which the mask is to be applied
    - maskfile: path to a file specifying the mask to be applied
    - average: if True, averaging should to be done when valueing the mask

    Returns:
    an image which the result of valueing the specified mask to src.
    """
    pass
