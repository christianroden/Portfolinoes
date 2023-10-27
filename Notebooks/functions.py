# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# horizontal divider line

def f_divline(pad_before=True, pad_after=True):
    '''Draws (prints) a simple horizontal line
    Args.:
        pad_before (bool): add pading before the line
        pad_after (bool): add padding after the line
    '''
    line = str('- '*40)
    if pad_before:
        line = '\n'+line
    if pad_after:
        line = line+'\n'
    
    return print(line)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -