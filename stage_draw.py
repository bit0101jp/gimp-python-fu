#!/usr/bin/env python
# -*- coding:utf-8 -*-

###画像生成、アニメGIF出力、GIMP終了

from gimpfu import *

#
# 描画
#
def layer_draw(layer, point_xy, point_nm):

# 描画色の設定
  maskcolor = (255,0,0,1.0)
  pdb.gimp_context_set_foreground((0, 0, 255))

# ペンサイズの設定
  pdb.gimp_context_set_brush_size(5.0)

# 線を描画
  pdb.gimp_pencil(layer, point_nm, point_xy)


#
# レイヤーの追加
#
def layer_add(img, pos, layer_name):

# レイヤーの追加(透明)
  layer = pdb.gimp_layer_new(img, 400, 190, RGB_IMAGE, layer_name, 100.0 , LAYER_MODE_NORMAL)

# 塗りつぶし色の設定
  pdb.gimp_drawable_fill(layer, FILL_TRANSPARENT)

# 画像データの 1 番目の位置にレイヤーを挿入する
  pdb.gimp_image_add_layer(img, layer, pos)

  return layer

#
# MAINサブルーチン
#
def routine(img, drawable, gifname):

# 画像データを生成
  img = pdb.gimp_image_new(400, 190, RGB)

# 生成した画像を表示
  pdb.gimp_display_new(img)

# GIFの最後にテキストレイヤを追加する
  text_layer = pdb.gimp_text_layer_new(img, "layer000", "Mochiy Pop E P Ultra-Bold", 0, 0)
  pdb.gimp_image_add_layer(img, text_layer, 0)
  text_layer = pdb.gimp_text_fontname(img, text_layer, 50.0, 10.0, "星はどこにある？", 1, TRUE, 36.0, 1, "Mochiy Pop E P Ultra-Bold")
  pdb.gimp_drawable_set_name(text_layer, "layer000" + "(600ms)(combine)")



  pos = 1

# レイヤーの追加
  for i in range(6):
    layer = layer_add(img, pos, "layer" + str(pos).zfill(3) + "(5ms)(combine)")
    x1 = i * 80.0
    x2 = i * 80.0 + 40
    y1 = 100.0  
    y2 = 150.0
    list = [x1, y1,  x1, y2,  x2, y2,  x2, y1,  x1, y1]  
    layer_draw(layer, list, 10)
    pos += 1

  for i in range(6, 0, -1):
    layer = layer_add(img, pos, "layer" + str(pos).zfill(3) + "(5ms)(combine)")
    x1 = i * 80.0 
    x2 = i * 80.0 + 40
    y1 = 100.0
    y2 = 150.0
    list = [x1, y1,  x1, y2,  x2, y2,  x2, y1,  x1, y1]  
    layer_draw(layer, list, 10)
    pos += 1

  for i in range(6):
    layer = layer_add(img, pos, "layer" + str(pos).zfill(3) + "(5ms)(combine)")
    pos += 1


#  text_layer = pdb.gimp_text_layer_new(img, "layer" + str(pos).zfill(3), "osaka", 0, 0)
#  pdb.gimp_image_add_layer(img, text_layer, pos)
#
##  pdb.gimp_text_layer_set_text(text_layer, "星はどこにある？")
#  text_layer = pdb.gimp_text_fontname(img, text_layer, 50.0, 10.0, "これはテストです。", 1, TRUE, 
#  36.0, 1, "osaka")
##  pdb.gimp_image_add_layer(img, text_layer, pos)
##  pdb.gimp_floating_sel_anchor(text_layer)
#  pdb.gimp_drawable_set_name(text_layer, "layer" + str(pos).zfill(3) +"(600ms)(combine)")



# 画面の再描画
  gimp.displays_flush()

# インデックス画像に変換
  pdb.gimp_convert_indexed(img, 0, 0, 255, FALSE, FALSE, "")

# アニメGIF出力
  pdb.file_gif_save( img, layer, gifname, gifname, 0, 0, 5, 1)


#
# MAINルーチン
#
def cup_generate(img, drawable, n, d):
  
  routine(img, drawable,  "⁨ddd1.gif")

# GIMP終了
##  pdb.gimp_quit(TRUE);




register(
  "stage_draw",
  "アニメGIFを自動生成します",
  "アニメGIFを自動生成します",
  "try",
  "try",
  "date",
  "<Image>/Python-fu/Layer/stage_draw",
  "*",
  [
   (PF_SPINNER, "n", "開始番号", 1, (0, 100, 1)),
   (PF_SPINNER, "d", "桁数", 1, (1, 100, 1))
   ],
  [],
  cup_generate)

main()