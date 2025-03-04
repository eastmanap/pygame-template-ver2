# color cycle function
col1 = 0
col2 = 0
col3 = 255
    
col1_ = True
col2_ = False
col3_ = False

if col1_:
    col1 += 1
    col3 -= 1
    if col1 == 255:
        col1_ = False
        col2_ = True
        
elif col2_:
    col2 += 1
    col1 -= 1
    if col2 == 255:
        col2_ = False
        col3_ = True

elif col3_:
    col3 += 1
    col2 -= 1
    if col3 == 255:
        col3_ = False
        col1_ = True






# Basic Colors
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
CYAN    = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Extended Colors
GRAY       = (128, 128, 128)
DARK_GRAY  = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)
ORANGE     = (255, 165, 0)
PURPLE     = (128, 0, 128)
BROWN      = (139, 69, 19)
PINK       = (255, 192, 203)
LIME       = (50, 205, 50)
TEAL       = (0, 128, 128)
NAVY       = (0, 0, 128)
GOLD       = (255, 215, 0)
INDIGO     = (75, 0, 130)
VIOLET     = (238, 130, 238)

# Web Colors
TOMATO      = (255, 99, 71)
CORAL       = (255, 127, 80)
SALMON      = (250, 128, 114)
TURQUOISE   = (64, 224, 208)
AQUA        = (0, 255, 255)
OLIVE       = (128, 128, 0)
MAROON      = (128, 0, 0)
STEEL_BLUE  = (70, 130, 180)
ROYAL_BLUE  = (65, 105, 225)
FOREST_GREEN = (34, 139, 34)

# Oddly Specific Colors
MIDNIGHT_PLUM          = (44, 12, 60)
UNSETTLING_GREEN       = (68, 163, 64)
GHOSTLY_LAVENDER       = (217, 203, 255)
OLD_PAPER_YELLOW       = (238, 232, 170)
WET_CONCRETE_GRAY      = (102, 102, 102)
TV_STATIC_WHITE        = (234, 234, 234)
DEEP_SEA_MYSTERY_BLUE  = (3, 45, 66)
FRESHLY_MOWED_GRASS    = (76, 175, 80)
GLITCHY_CYAN           = (0, 250, 180)
SUN_FADED_NEON_PINK    = (255, 90, 120)
ANCIENT_SCROLL_BEIGE   = (189, 155, 108)
SYNTHWAVE_PURPLE       = (160, 32, 240)
FIZZY_LEMON            = (253, 255, 129)
DIM_COMPUTER_SCREEN    = (30, 30, 40)
SLIGHTLY_ANNOYING_ORANGE = (255, 140, 0)
MOONLIT_SHADOW           = (25, 25, 50)
OVERLY_SPECIFIC_BLUE     = (23, 92, 187)

# Extra Oddly Specific Colors
YOUTUBE_AD_RED = (200, 20, 20)
DISCORD_MOD_PURPLE = (114, 137, 218)
FROZEN_PEAS_GREEN = (120, 200, 80)
BATHROOM_TILE_BLUE = (180, 215, 230)
WINDOWS_XP_GRASS_GREEN = (105, 190, 69)
DEEP_FRIED_MEME_YELLOW = (255, 224, 102)
EARLY_WEBSITE_BLUE = (0, 153, 204)
OBNOXIOUS_HIGHLIGHTER_PINK = (255, 0, 128)
SLIGHTLY_USED_ERASER_PINK = (255, 182, 193)
WEIRDLY_SATURATED_SKY_BLUE = (50, 200, 255)
ARTIFICIAL_BANANA_YELLOW = (255, 225, 53)
