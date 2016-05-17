from alien_keytree import Tree

hw_key = "H GgG d gGg e ggG l GGg o gGG r Ggg w ggg a gG"
hw_test = "GgGggGGGgGGggGG, ggggGGGggGGggGg!"

real_key = "C GgggGgg H GgggGgG T GgggGGg a gGg c GGggG d GggG e GgG g ggGgG h GGgGg i gGGg j GgggGGG l gGGG m ggGGg n GGgGG o ggg p ggGGG r GGGg s GGGG t GGgggG u ggGgg v Ggggg w GGggggg y GGggggG"
real_test = "GgggGGgGGgGggGGgGGGG GGggGGGgGggGggGGGgGGGGgGGGgGGggGgGGgG GGggggggGgGGGG ggGGGGGGggggggGGGgggGGGGGgGGggG gGgGGgGGGggG GggGgGGgGGGGGGggGggGggGGGGGGGGGgGGggG gggGggggGgGGGGg gGgGGgggG /GGGg/GggGgGggGGggGGGGGggggGggGGGGGGggggggGgGGGGggGgggGGgggGGgGgGGGGg_gGGgGggGGgGgGgGGGG. GgggGgGgGgGggggGgG gGg GGggGgggggggGGG GGggGGGgGggGggGGGgGGGGgGGGgGGggGgGGgG gGGgGggGGgGgGg? GgggGgggggggGGgGgG GgggGGGggggGGgGGgGG ggGggGGGG gggGggggGgGGGGg GGgggGGGgGgGgGGGGgGgG!"

pbreen_key = "D GgggGgg p gGGg d GgggGGg y gGg o GGggG h ggGgG i GGgGg a GgggGgG s GgggGGG c GgG r GggG"
pbreen_test = "GgggGggGgggGgGGgggGGgGgggGGggGg GGggGGggG GgGggGgGGGgGggGGgGgggGGG?"

def decode(key, subject):
    root = Tree(key)
    # print root.str_tree()
    translation = root.decode(subject)
    print translation
        
decode(hw_key, hw_test)
decode(real_key, real_test)
decode(pbreen_key, pbreen_test)