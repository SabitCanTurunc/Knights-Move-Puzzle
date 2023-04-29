import pygame
import random

# Renk Tanımlama
Siyah = (0, 0, 0)
Beyaz = (255, 255, 255)
Yesil = (0, 255, 0)
Kirmizi = (255, 0, 0)

def tahta_olustur(size):
    tahta = [[0 for x in range(size)] for y in range(size)]
    return tahta

def tahtaya_yaz(tahta):
    for row in tahta:
        print(" ".join(str(cell) for cell in row))

def rastgele_konum(size):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return x, y

def mevcut_hareket(tahta, x, y, size):
    if x < 0 or x >= size or y < 0 or y >= size:
        return False
    if tahta[x][y] != 0:
        return False
    return True
def gecerli_hareket_sayisi(tahta, x, y, size):
    move_counts = [[len(gecerli_hareket(tahta, i, j, size)) for j in range(size)] for i in range(size)]
    return move_counts
def gecerli_hareket(tahta, x, y, size):
    moves = []
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if mevcut_hareket(tahta, nx, ny, size):
            moves.append((nx, ny))
    return moves

def ana_tahta(screen, tahta, size):
    hucre_boyutu = 50
    border_width = 1
    for i in range(size):
        for j in range(size):
            x = j * hucre_boyutu
            y = i * hucre_boyutu
            if tahta[i][j] == 0:
                pygame.draw.rect(screen, Beyaz, [x, y, hucre_boyutu, hucre_boyutu])
                pygame.draw.rect(screen, Siyah, [x, y, hucre_boyutu, hucre_boyutu], border_width)
            else:
                pygame.draw.rect(screen, Yesil, [x, y, hucre_boyutu, hucre_boyutu])
                font = pygame.font.Font(None, 36)
                text = font.render(str(tahta[i][j]), True, Siyah)
                text_rect = text.get_rect(center=(x+hucre_boyutu/2, y+hucre_boyutu/2))
                screen.blit(text, text_rect)


def main():
    # oyuna başlama
    pygame.init()

    # tahtayı ayarlama
    size = int(input("Tahta boyutunu girin: "))
    hucre_boyutu = 50
    width = size * hucre_boyutu
    height = size * hucre_boyutu
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Kare Defter")


    # oyun tahtasını oluşturma
    tahta = tahta_olustur(size)
    x, y = rastgele_konum(size)
    tahta[x][y] = 1
    ana_tahta(screen, tahta, size)
    pygame.display.update()

    # Oyun döngüsünü ayarlama
    skor = 0
    max_skor = size**2
    calisiyorMu = True
    while calisiyorMu:
        # Hareket ve fonksiyonlar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                calisiyorMu = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x_new = pos[1] // hucre_boyutu
                y_new = pos[0] // hucre_boyutu
                moves = gecerli_hareket(tahta, x, y, size)

                if (x_new, y_new) in moves:
                    # tahtayı güncelle
                    skor += 1
                    tahta[x_new][y_new] = skor + 1
                    x, y = x_new, y_new
                    ana_tahta(screen, tahta, size)
                    pygame.display.update()

                    # oyun bitti mi (kontrol)
                    if skor == max_skor - 1:
                        font = pygame.font.Font(None, 36)
                        text = font.render("You won!", True, Kirmizi)
                        text_rect = text.get_rect(center=(width / 2, height / 2))
                        screen.blit(text, text_rect)
                        pygame.display.update()
                        pygame.time.wait(3000)
                        calisiyorMu = False
                else:
                    font = pygame.font.Font(None, 36)
                    text = font.render(f"Invalid move skor: {(skor+1)*4}", True, Kirmizi)
                    text_rect = text.get_rect(center=(width / 2, height / 2))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    pygame.time.wait(1000)

                    # oyundan cık
pygame.quit()
if __name__ == "__main__":
    main()

