import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#背景画像Surfaceを作成する
    bg_img_r = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")#こうかとんSurfaceaを作成する
    kk_img = pg.transform.flip(kk_img, True, False)#こうかとん左右反転させる
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr%3200)

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img_r,[x+1600,0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img, [x+4800, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()