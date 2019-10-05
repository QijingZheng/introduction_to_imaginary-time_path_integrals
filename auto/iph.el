(TeX-add-style-hook
 "iph"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("beamer" "8pt" "dvipsnames")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("caption" "font={small,sf}" "labelfont={bf}" "labelsep=endash")))
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "beamer"
    "beamer10"
    "tikz"
    "caption"
    "sansmath"
    "xcolor"
    "graphicx"
    "framed"
    "amsmath"
    "amssymb"
    "siunitx"
    "mathabx"
    "tasks"
    "multicol"
    "braket"
    "datetime")
   (TeX-add-symbols
    '("colvec" ["argument"] 2)
    '("info" ["argument"] 3)
    '("tikzmark" 1)
    '("rom" 1)
    '("BOsup" 0)
    '("onehalf" 0)
    '("dt" 1)
    '("Rvec" 0)
    '("svec" 0)
    '("rvec" 0)
    '("hamil" 0)
    "angstrom"
    "rt"
    "rR"
    "prR"
    "Rt"
    "rRt"
    "EYSR"
    "DPSR"
    "shortminus"
    "ua"
    "da"
    "uda"
    "uua"
    "dda"
    "dua"
    "eps"
    "nac"
    "soc"
    "mathcolor")
   (LaTeX-add-labels
    "eq:bloch_soc"
    "eq:soc_mf"
    "eq:hamil_soc"
    "eq:soc_paw1"
    "eq:soc_paw2"
    "eq:scf"
    "eq:nscf-diag"
    "eq:soc_paw_again"
    "eq:Yij_eval"
    "eq:mae_def"
    "eq:schro"
    "eq:tot_hamil"
    "eq:wfc_exp"
    "eq:coeffi_eq"
    "eq:spin-adiabatic-rep"
    "eq:pjk"
    "eq:phi_decomp"
    "eq:sh_matrix1"
    "eq:st_mat_ele"
    "eq:phi_decomp_2"
    "eq:sh_matrix2"
    "eq:nac_spinor")
   (LaTeX-add-xcolor-definecolors
    "MidnightBlue"))
 :latex)

