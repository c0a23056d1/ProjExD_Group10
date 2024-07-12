import math
import os
import random
import sys
import time
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


WIDTH = 1100
HEIGHT = 650

def check_bound(obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し，真理値タプルを返す関数
    引数：こうかとんや爆弾，ビームなどのRect
    戻り値：横方向，縦方向のはみ出し判定結果（画面内：True／画面外：False）
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

class Allen(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load("fig/スクリーンショット 2024-07-09 145858.png"), 0, 0.9)
        self.rect = self.image.get_rect()
        self.rect.center = 300, 200
        self.gravity = 1
        self.velocity = 0
        self.on_ground = True


    
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.on_ground:
            self.velocity = self.jump_speed
            self.on_ground = False

        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0
            self.on_ground = True

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1200, 700))
    clock  = pg.time.Clock()
    beamallen = None
    #背景画像をロードして、ウインドウのサイズにリサイズ
    back_img = pg.image.load("fig/24535830.jpg") 
    back_img = pg.transform.scale(back_img, (1200, 700))
    allen = Allen((100, 600))
    show_allen = True
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                show_allen = not show_allen #アレンの表示非表示の切替(キャラの切り替えで使うかも)
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                # スペースキー押下でBeamクラスのインスタンス生成
                beamallen = BeamAllen(allen)
        
        screen.blit(back_img, [0, 0]) #背景画像を表すsurfase
       
        key_lst = pg.key.get_pressed()
        if show_allen:
            allen.update(key_lst, screen)
        if beamallen is not None:
            beamallen.update(screen)

        pg.display.update()
        clock.tick(60)

 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()