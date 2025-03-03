# List of Green Valley Bible Camp camp songs we know
import random

gvbcSongBookDictionary = {
    1: 'A Common Love',
    4: 'All in All',
    9: 'As the Deer (Old)',
   10: 'Awesome God',
   12: 'Battle Belongs to the Lord',
   13: 'Be Still and Know',
   19: 'Blue Skies and Rainbows',
   23: 'Come Let Us Sing',
   27: 'Create in Me a Clean Heart',
   29: 'Deep Down in My Heart',
   35: 'Father I Adore You',
   38: 'Freely, Freely',
   42: 'Glorify Thy Name',
   44: 'God Is So Good',
   48: 'Greatest Commands',
   52: 'Have You Seen Jesus My Lord',
   53: 'He Has Made Me Glad',
   56: 'He Is My Everything',
   58: 'He Paid a Debt',
   62: 'Hear O Israel',
   69: 'His Name Is Wonderful',
   70: 'Holy Ground',
   80: 'Humble Yourself',
   82: 'I Am Mine Nomore',
   85: 'I Love You Lord',
   86: 'We Love You with the Love of the Lord',
   87: 'I Stand in Awe',
   88: 'I Want Jesus to Walk with Me',
   89: 'I Want to Know Christ',
   90: 'I Will Call upon the Lord',
   92: 'I\'m Happy Today',
   93: 'I\'ve Been Crucified with Christ',
   94: 'I\'ve Got Peace Like a River',
   95: 'I\'ve Got the Joy',
  100: 'Jesus Is Lord',
  101: 'Jesus Keep Me Near the Cross (New)',
  102: 'Jesus Let Us Come to Know You',
  104: 'Jesus, Name Above All Names',
  114: 'Livin\' on the Lord\'s Side',
  115: 'Lord Be There',
  116: 'Lord Has a Will',
  117: 'Lord We Lift Your Name on High',
  121: 'Love, Love, Love, Love',
  124: 'Majesty',
  125: 'Make Me a Servant',
  128: 'May I Call You Father',
  133: 'On Bended Knee',
  135: 'Pass It On',
  136: 'Pierce My Ear',
  137: 'Praise the Name of Jesus',
  141: 'Rejoice in the Lord Always',
  142: 'Restore My Spirit Lord',
  146: 'Seek Ye First',
  150: 'Sing Hallelujah to the Lord',
  151: 'Someday',
  152: 'Soon and Very Soon',
  153: 'Steadfast Love of the Lord',
  154: 'Step by Step',
  156: 'Teach Me, Lord, to Wait',
  163: 'They\'ll Know We Are Christians',
  164: 'This Is the Day',
  166: 'Thy Word',
  169: 'Unto Thee, O Lord',
  170: 'Victory Chant',
  171: 'We Bow Down',
  174: 'We Shall Assemble',
  175: 'We Will Glorify',
  182: 'Wonderful, Wonderful',
  183: 'Worthy Is the Lamb',
  184: 'You Are the Song that I Sing',
}

# print(gvbcSongBookDictionary)
# 
for n in range(5):
    index = random.randint(0, len(gvbcSongBookDictionary.values()) - 1)
    item = list(gvbcSongBookDictionary.items())[index]
    print(str(item[0]) + "   " + str(item[1]))

# gvbcList = []
# for k, v in gvbcSongBookDictionary.items():
#     gvbcList += [str(k) + "   " + str(v)]
# print(gvbcList)

# Learning to iterate with the multiple assignment trick to compose a list, I found an interesting bug.
# When the brackets aren't placed arond the item to add to the list, and you just add the string,
# then the string is converted to a list of letters. That list is added to the list. So each separate
# symbol in what you intended to be a list item is added as a list item itself. Thus, instead of an
# iteration over {'one':'red','two':'blue'} yielding ['one red', 'two blue'], it gives
# ['o', 'n', 'e', ' ', 'r', 'e', 'd', 't', 'w', 'o', ' ', 'b', 'l', 'u', 'e']
# myNewList = []
# for k,v in {'one':'red','two':'blue'}.items():
#     myNewList += [str(k) + " " + str(v)]
# print(myNewList)
# myNewList = []
# for k,v in {'one':'red','two':'blue'}.items():
#     myNewList += str(k) + " " + str(v)             # This should have been within brackets.
# print(myNewList)
# bug doc: to add a string to a list, verify bracket enclosure

gvbcSongBookList = [
	'A Common Love',
	'All in All',
	'As the Deer (Old)',
	'Awesome God',
	'Battle Belongs to the Lord',
	'Be Still and Know',
	'Blue Skies and Rainbows',
	'Come Let Us Sing',
	'Create in Me a Clean Heart',
	'Deep Down in My Heart',
	'Father I Adore You',
	'Freely, Freely',
	'Glorify Thy Name',
	'God Is So Good',
	'Greatest Commands',
	'Have You Seen Jesus My Lord',
	'He Has Made Me Glad',
	'He Is My Everything',
	'He Paid a Debt',
	'Hear O Israel',
	'His Name Is Wonderful',
	'Holy Ground',
	'Humble Yourself',
	'I Am Mine Nomore',
	'I Love You Lord',
	'We Love You with the Love of the Lord',
	'I Stand in Awe',
	'I Want Jesus to Walk with Me',
	'I Want to Know Christ',
	'I Will Call upon the Lord',
	'I\'m Happy Today',
	'I\'ve Been Crucified with Christ',
	'I\'ve Got Peace Like a River',
	'I\'ve Got the Joy',
	'Jesus Is Lord',
	'Jesus Keep Me Near the Cross (New)',
	'Jesus Let Us Come to Know You',
	'Jesus, Name Above All Names',
	'Livin\' on the Lord\'s Side',
	'Lord Be There',
	'Lord Has a Will',
	'Lord We Lift Your Name on High',
	'Love, Love, Love, Love',
	'Majesty',
	'Make Me a Servant',
	'May I Call You Father',
	'On Bended Knee',
	'Pass It On',
	'Pierce My Ear',
	'Praise the Name of Jesus',
	'Rejoice in the Lord Always',
	'Restore My Spirit Lord',
	'Seek Ye First',
	'Sing Hallelujah to the Lord',
	'Someday',
	'Soon and Very Soon',
	'Steadfast Love of the Lord',
	'Step by Step',
	'Teach Me, Lord, to Wait',
	'They\'ll Know We Are Christians',
	'This Is the Day',
	'Thy Word',
	'Unto Thee, O Lord',
	'Victory Chant',
	'We Bow Down',
	'We Shall Assemble',
	'We Will Glorify',
	'Wonderful, Wonderful',
	'Worthy Is the Lamb',
	'You Are the Song that I Sing',
]
# for n in range(5):
#     print(gvbcSongBookList[random.randint(0, len(gvbcSongBookList) - 1)])

