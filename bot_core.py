# Chess bot, created by BOB BOBBIE BOBBERSON using Stockfish and Selenium

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from stockfish import Stockfish
import time
import keyboard

driver = webdriver.Edge()
driver.get('https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2F')

# define variables
user = "defaultuser"
passw = "defaultpassword"
stockfish = Stockfish("stockfish.exe", parameters={"Threads": 2, "Slow Mover": 76})
chessboard = []
stockfish.set_skill_level(25)
stockfish.set_depth(23)


# get the user credentials
def getCredentials():
    global user
    global passw
    print("Chess.com Login")
    user = input("Enter username or email: ")
    passw = input("Enter password: ")


getCredentials()


# sign in using username and password
def signin(u, p):
    username = driver.find_element_by_name("_username")
    username.send_keys(u)

    password = driver.find_element_by_name("_password")
    password.send_keys(p)

    loginbutton = driver.find_element_by_name("login")
    loginbutton.click()


signin(user, passw)

driver.get("https://www.chess.com/play/computer")


def getMove(side):
    chesselement = driver.find_element_by_tag_name("chess-board")
    pieceslist = chesselement.find_elements_by_tag_name("div")
    coordinates_dictionary = {
        "18": "1",
        "28": "2",
        "38": "3",
        "48": "4",
        "58": "5",
        "68": "6",
        "78": "7",
        "88": "8",

        "17": "9",
        "27": "10",
        "37": "11",
        "47": "12",
        "57": "13",
        "67": "14",
        "77": "15",
        "87": "16",

        "16": "17",
        "26": "18",
        "36": "19",
        "46": "20",
        "56": "21",
        "66": "22",
        "76": "23",
        "86": "24",

        "15": "25",
        "25": "26",
        "35": "27",
        "45": "28",
        "55": "29",
        "65": "30",
        "75": "31",
        "85": "32",

        "14": "33",
        "24": "34",
        "34": "35",
        "44": "36",
        "54": "37",
        "64": "38",
        "74": "39",
        "84": "40",

        "13": "41",
        "23": "42",
        "33": "43",
        "43": "44",
        "53": "45",
        "63": "46",
        "73": "47",
        "83": "48",

        "12": "49",
        "22": "50",
        "32": "51",
        "42": "52",
        "52": "53",
        "62": "54",
        "72": "55",
        "82": "56",

        "11": "57",
        "21": "58",
        "31": "59",
        "41": "60",
        "51": "61",
        "61": "62",
        "71": "63",
        "81": "64",
    }
    fen_pieces = {
        "wr": "R",
        "wn": "N",
        "wb": "B",
        "wq": "Q",
        "wk": "K",
        "wp": "P",

        "br": "r",
        "bn": "n",
        "bb": "b",
        "bq": "q",
        "bk": "k",
        "bp": "p",
    }
    dictionary = []
    numbers = []

    for x in pieceslist:
        if x.get_attribute('class').startswith('highlight') or x.get_attribute('class').startswith(
                'hover') or x.get_attribute('class').startswith('assist') or fen_pieces[
            x.get_attribute("class")[6] + x.get_attribute("class")[7]] == 'io' or str(
            x.get_attribute("class")[-2] + x.get_attribute("class")[-1]) == 'ng':
            pass
        else:
            dictionary.append(fen_pieces[x.get_attribute("class")[6] + x.get_attribute("class")[7]])
            numbers.append(coordinates_dictionary[str(x.get_attribute("class")[-2] + x.get_attribute("class")[-1])])

    fenlist = []

    for x in range(1, 65):
        if str(x) in numbers:
            fenlist.append(dictionary[numbers.index(str(x))])
        else:
            fenlist.append('1')

    fen_without_slashes = ''.join(fenlist)

    counter = 0
    for x in range(1, len(fen_without_slashes)):
        if x % 8 == 0:
            fenlist.insert(x + counter, '/')
            counter += 1
            # add slash

    ###########################################################
    ###################     GET FEN     #######################
    FEN = ''.join(fenlist), 'w'
    ###################     GET FEN     #######################
    ###########################################################

    stockfish.set_fen_position(str(''.join(fenlist)) + ' ' + side)
    bestmove = stockfish.get_best_move()
    print(bestmove)

    fencoordinates = {
        'a1': '11',
        'b1': '21',
        'c1': '31',
        'd1': '41',
        'e1': '51',
        'f1': '61',
        'g1': '71',
        'h1': '81',

        'a2': '12',
        'b2': '22',
        'c2': '32',
        'd2': '42',
        'e2': '52',
        'f2': '62',
        'g2': '72',
        'h2': '82',

        'a3': '13',
        'b3': '23',
        'c3': '33',
        'd3': '43',
        'e3': '53',
        'f3': '63',
        'g3': '73',
        'h3': '83',

        'a4': '14',
        'b4': '24',
        'c4': '34',
        'd4': '44',
        'e4': '54',
        'f4': '64',
        'g4': '74',
        'h4': '84',

        'a5': '15',
        'b5': '25',
        'c5': '35',
        'd5': '45',
        'e5': '55',
        'f5': '65',
        'g5': '75',
        'h5': '85',

        'a6': '16',
        'b6': '26',
        'c6': '36',
        'd6': '46',
        'e6': '56',
        'f6': '66',
        'g6': '76',
        'h6': '86',

        'a7': '17',
        'b7': '27',
        'c7': '37',
        'd7': '47',
        'e7': '57',
        'f7': '67',
        'g7': '77',
        'h7': '87',

        'a8': '18',
        'b8': '28',
        'c8': '38',
        'd8': '48',
        'e8': '58',
        'f8': '68',
        'g8': '78',
        'h8': '88',
    }
    coordinate = fencoordinates[bestmove[0] + bestmove[1]]
    print(coordinate)

    coordinate2 = fencoordinates[bestmove[2] + bestmove[3]]

    driver.execute_script("document.querySelectorAll('.assist').forEach(e => e.remove());")
    driver.execute_script(
        "document.getElementsByClassName('board')[0].insertAdjacentHTML(\"beforeend\", \"<div class='assist highlight square-" + coordinate + "' style='background-color: rgb(255, 0, 0); opacity: 0.5;' width='1px' height='1px'></div>\");")
    driver.execute_script(
        "document.getElementsByClassName('board')[0].insertAdjacentHTML(\"beforeend\", \"<div class='assist highlight square-" + coordinate2 + "' style='background-color: rgb(255, 0, 0); opacity: 0.5;' width='1px' height='1px'></div>\");")


while True:
    if keyboard.is_pressed('ctrl+y'):
        getMove('w')
    if keyboard.is_pressed('ctrl+q'):
        getMove('b')
