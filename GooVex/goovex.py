#!/usr/bin/python
######################################################################
#  A GnoTravex like program in Python with the goocanvas.
#
#  Dov Grobgeld <dov.grobgeld@gmail.com>
#
#  This program is licensed under the GPL.
#
#  Todo:
#  * Make more decorations.
#  * Time the solution.
#  * Keep high-score.
#  * Indicate when the user solves the puzzle.
#
#  Version: 0.1.0
# 
######################################################################

import gtk
from gtk import keysyms
import math
import goocanvas
import random

# The numeric contents of a tile
class Tile:
  def __init__(self):
    self.n=int(random.random()*10)
    self.e=int(random.random()*10)
    self.s=int(random.random()*10)
    self.w=int(random.random()*10)

# VexTile contains the playable pieces of the game.
class VexTile(goocanvas.Group):
  def __init__(self,
               parent,
               num_north,
               num_west,
               num_south,
               num_east,
               x0,
               y0,
               tile_size) :
    goocanvas.Group.__init__(self,parent=parent)
    s=tile_size # shortcut
    s2=s/2
    st=s/3    # text position

    # Declare the four triangles that make up a tile for
    # the four directions.
    poly=[
        [(-s2,-s2), 
         (+s2,-s2), 
         (0,0), 
         (-s2,-s2)],
        [(0,0),
         (+s2,-s2),
         (+s2,+s2),
         (0,0)],
        [(0,0),
         (+s2,+s2),
         (-s2,+s2),
         (0,0)],
        [(0,0),
         (-s2,s2),
         (-s2,-s2),
         (0,0)]]
    text_pos = [(0,-st),
                (st,0),
                (0,st),
                (-st,0)]

    # Turn the directions into a  array
    self.tile_nums = [num_north,num_west,num_south,num_east]

    # Create the four triangles
    for i in range(4):
      bg,fg=self.get_triangle_color(self.tile_nums[i])
      p = goocanvas.Points (poly[i])
      tile =  goocanvas.Polyline(parent=self,
                                 points=p,
                                 close_path=True,
                                 fill_color=bg,
                                 stroke_pattern=None)
    # Put text on the triangles
    font_size = 1.0*tile_size / 100 * 24
    for i in range(4):
      bg,fg=self.get_triangle_color(self.tile_nums[i])
      item = goocanvas.Text (parent=self,
                             text="%d"%self.tile_nums[i], 
                             x=text_pos[i][0], 
                             y=text_pos[i][1], 
                             anchor=gtk.ANCHOR_CENTER,
                             font = "Sans Bold %.0f"%font_size,
                             fill_color=fg
                             )
    self.translate(x0,y0)

  # Return the color corresponding to a number
  def get_triangle_color(self,num):
    res_colors = [("black","white"),
            ("brown","black"),
            ("red","black"),
            ("orange","black"),
            ("yellow","black"),
            ("green","black"),
            ("blue","white"),
            ("violet","black"),
            ("grey45","white"),
            ("gray90","black")]
    return res_colors[num]


# This is the game class
class Goovex(gtk.Window):
  def setup_item_signals (self, item):
    item.connect ("motion_notify_event", self.on_motion_notify)
    item.connect ("button_press_event", self.on_button_press)
    item.connect ("button_release_event", self.on_button_release)

  def on_motion_notify (self, item, target, event):
    if (self.dragging == True) and (event.state & gtk.gdk.BUTTON1_MASK):
      new_x = event.x
      new_y = event.y
      item.translate (new_x - self.drag_x, new_y - self.drag_y)
    return True

  def on_button_press (self, item, target, event):
    item.raise_(None)
    self.drag_x = event.x
    self.drag_y = event.y

    fleur = gtk.gdk.Cursor (gtk.gdk.FLEUR)
    canvas = item.get_canvas ()
    canvas.pointer_grab (item,
               gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_RELEASE_MASK,
               fleur,
               event.time)
    self.dragging = True
    return True

  def on_button_release (self, item, target, event):
    canvas = item.get_canvas ()
    canvas.pointer_ungrab (item, event.time)
    self.dragging = False
    # Quantize pos of group
    trans = item.get_transform()

    x = trans[4]
    y = trans[5]

    xsubtract = self.xmargin+self.tile_size/2
    ysubtract = self.ymargin+self.tile_size/2

    if x > self.xmargin + self.tile_size * (0.5+self.board_size):
      xsubtract += self.xmargin + self.board_size*self.tile_size

    x-= xsubtract
    y-= ysubtract
    
    # The following complex math was created in order to make
    # tile always fall on top of the board.
    xq = (math.floor(x/self.tile_size+0.5))*self.tile_size
    yq = (math.floor(y/self.tile_size+0.5))*self.tile_size
    xq+= xsubtract
    yq+= ysubtract
    trans.translate(xq-trans[4],yq-trans[5])
    item.set_transform(trans)
    # TBD place the tile on the board

  # Create a random board. 
  def get_board(self, board_size):
    board=[]
    for i in range(board_size*board_size):
      board.append(Tile())
    # Make adjacent numbers the same using some clever looping
    for i in range(1,board_size):
      for j in range(board_size):
        board[j*board_size+i].w=board[j*board_size+(i-1)].e
        board[i*board_size+j].n=board[(i-1)*board_size+j].s
    # Shuffle 100 times
    for i in range(100):
      p1=int(random.random()*board_size*board_size)
      p2=int(random.random()*board_size*board_size)
      if p1!=p2:
        tmp=board[p1]
        board[p1]=board[p2]
        board[p2]=tmp
    return board

  # Erase the current pieces and create new ones
  def new_game(self, board_size):
    root = self.canvas.get_root_item()
    board = self.get_board(board_size)
    self.tile_size = 300/board_size
    self.board_size = board_size

    # Erase the old board
    for t in self.tiles:
      idx=root.find_child(t)
      if idx!=1:
        root.remove_child(idx)
    self.tiles = []

    for g in self.grid:
      root.remove_child(g)

    # Create new board
    for j in range(board_size):
      for i in range(board_size):
        p = j*board_size+i
        w,n,e,s = board[p].w,board[p].n,board[p].e,board[p].s
        ht = VexTile(root, n,e,s,w,
                     2*self.xmargin + self.tile_size*(board_size+i+0.5),
                     1*self.ymargin + self.tile_size*(j+0.5),
                     self.tile_size)
        self.setup_item_signals(ht)
        self.tiles.append(ht)

    # create destination grid
    self.grid = []
    for i in range(board_size+1):
      self.grid += [goocanvas.Rect(parent=root,
                                   x=self.xmargin+i*self.tile_size-1,
                                   y=self.ymargin,
                                   width=2,
                                   height=board_size*self.tile_size,
                                   fill_color="gray50",
                                   stroke_color="none",
                                   line_width=0),
                    
                    goocanvas.Rect(parent=root,
                                   y=self.ymargin+i*self.tile_size-1,
                                   x=self.xmargin,
                                   height=2,
                                   width=board_size*self.tile_size,
                                   fill_color="gray50",
                                   stroke_color=None,
                                   line_width=0)]

  def is_solved(self):
    """Check if the game has been solved - Pending creation of a board"""
      

  def LetterButton(self,
                   parent=None,
                   color="pink",
                   text_color="black",
                   x=0,
                   y=0,
                   size=80,
                   text="",
                   cb=None):
      """A generic letter button"""
      bg = goocanvas.Group(parent = parent,
                           x=x,
                           y=y)
      goocanvas.Rect(parent = bg,
                     x=0,
                     y=0,
                     width=size,
                     height=size,
                     fill_color=color)
      goocanvas.Text(parent = bg,
                     anchor=gtk.ANCHOR_CENTER,
                     x=size/2,
                     y=size/2,
                     font="Sans Bold %.0f"%(1.0*size*3/4),
                     text=text,
                     fill_color=text_color)
      if not cb is None:
        bg.connect("button_press_event",cb)

  def Quit(*args):
    exit()

  def NewGame(self,*args):
    self.new_game(board_size=self.board_size)

  def NewGame2(self,*args):
    self.new_game(board_size=2)

  def NewGame3(self,*args):
    self.new_game(board_size=3)
  def NewGame4(self,*args):
    self.new_game(board_size=4)
  def NewGame5(self,*args):
    self.new_game(board_size=5)

  def __init__(self):
    gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
    self.xmargin=50
    self.ymargin=25
    self.connect("delete_event", self.Quit)
    self.dragging = False
    self.pickedup_tile = None
    vbox = gtk.VBox()
    self.add(vbox)
    self.canvas = goocanvas.Canvas()
    self.canvas.set_size_request(800,420)
    self.canvas.set_bounds(0,0,1200,1000)
    vbox.pack_start(self.canvas, True, True, 0)
    root = self.canvas.get_root_item()
    gtk.Widget.grab_focus(self.canvas)
    self.LetterButton(parent=root,
                      color="Maroon",
                      text="Q",
                      x=40,y=420-80,
                      cb = self.Quit)
    self.LetterButton(parent=root,
                      color="green",
                      text="2",
                      x=40+90*1,y=420-80,
                      cb = self.NewGame2)
    self.LetterButton(parent=root,
                      color="Lawn Green",
                      text="3",
                      x=40+90*2,y=420-80,
                      cb = self.NewGame3)
    self.LetterButton(parent=root,
                      color="yellowgreen",
                      text="4",
                      x=40+90*3,y=420-80,
                      cb = self.NewGame4)
    self.LetterButton(parent=root,
                      color="Lime Green",
                      text="5",
                      x=40+90*4,y=420-80,
                      cb = self.NewGame5)

    self.show_all()
    self.tiles=[]
    self.grid = []
    self.new_game(board_size=3) 

goovex = Goovex()
gtk.main()
