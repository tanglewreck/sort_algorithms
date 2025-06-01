let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <SNR>53_AutoPairsReturn =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsReturn')
inoremap <silent> <Plug>(ale_complete) :ALEComplete
cnoremap <silent> <Plug>(ale_show_completion_menu) <Nop>
inoremap <silent> <Plug>(ale_show_completion_menu) 
nnoremap  
nnoremap <NL> <NL>
nnoremap  
nnoremap  
xmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
xnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
nnoremap <silent> <Plug>(ale_info_preview) :ALEInfo -preview
nnoremap <silent> <Plug>(ale_info_clipboard) :ALEInfo -clipboard
nnoremap <silent> <Plug>(ale_info_echo) :ALEInfo -echo
nnoremap <silent> <Plug>(ale_info) :ALEInfo
nnoremap <silent> <Plug>(ale_repeat_selection) :ALERepeatSelection
nnoremap <silent> <Plug>(ale_code_action) :ALECodeAction
nnoremap <silent> <Plug>(ale_filerename) :ALEFileRename
nnoremap <silent> <Plug>(ale_rename) :ALERename
nnoremap <silent> <Plug>(ale_import) :ALEImport
nnoremap <silent> <Plug>(ale_documentation) :ALEDocumentation
nnoremap <silent> <Plug>(ale_hover) :ALEHover
nnoremap <silent> <Plug>(ale_find_references) :ALEFindReferences
nnoremap <silent> <Plug>(ale_go_to_implementation_in_vsplit) :ALEGoToImplementation -vsplit
nnoremap <silent> <Plug>(ale_go_to_implementation_in_split) :ALEGoToImplementation -split
nnoremap <silent> <Plug>(ale_go_to_implementation_in_tab) :ALEGoToImplementation -tab
nnoremap <silent> <Plug>(ale_go_to_implementation) :ALEGoToImplementation
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_vsplit) :ALEGoToTypeDefinition -vsplit
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_split) :ALEGoToTypeDefinition -split
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_tab) :ALEGoToTypeDefinition -tab
nnoremap <silent> <Plug>(ale_go_to_type_definition) :ALEGoToTypeDefinition
nnoremap <silent> <Plug>(ale_go_to_definition_in_vsplit) :ALEGoToDefinition -vsplit
nnoremap <silent> <Plug>(ale_go_to_definition_in_split) :ALEGoToDefinition -split
nnoremap <silent> <Plug>(ale_go_to_definition_in_tab) :ALEGoToDefinition -tab
nnoremap <silent> <Plug>(ale_go_to_definition) :ALEGoToDefinition
nnoremap <silent> <Plug>(ale_fix) :ALEFix
nnoremap <silent> <Plug>(ale_detail) :ALEDetail
nnoremap <silent> <Plug>(ale_lint) :ALELint
nnoremap <silent> <Plug>(ale_reset_buffer) :ALEResetBuffer
nnoremap <silent> <Plug>(ale_disable_buffer) :ALEDisableBuffer
nnoremap <silent> <Plug>(ale_enable_buffer) :ALEEnableBuffer
nnoremap <silent> <Plug>(ale_toggle_buffer) :ALEToggleBuffer
nnoremap <silent> <Plug>(ale_reset) :ALEReset
nnoremap <silent> <Plug>(ale_disable) :ALEDisable
nnoremap <silent> <Plug>(ale_enable) :ALEEnable
nnoremap <silent> <Plug>(ale_toggle) :ALEToggle
nnoremap <silent> <Plug>(ale_last) :ALELast
nnoremap <silent> <Plug>(ale_first) :ALEFirst
nnoremap <silent> <Plug>(ale_next_wrap_warning) :ALENext -wrap -warning
nnoremap <silent> <Plug>(ale_next_warning) :ALENext -warning
nnoremap <silent> <Plug>(ale_next_wrap_error) :ALENext -wrap -error
nnoremap <silent> <Plug>(ale_next_error) :ALENext -error
nnoremap <silent> <Plug>(ale_next_wrap) :ALENextWrap
nnoremap <silent> <Plug>(ale_next) :ALENext
nnoremap <silent> <Plug>(ale_previous_wrap_warning) :ALEPrevious -wrap -warning
nnoremap <silent> <Plug>(ale_previous_warning) :ALEPrevious -warning
nnoremap <silent> <Plug>(ale_previous_wrap_error) :ALEPrevious -wrap -error
nnoremap <silent> <Plug>(ale_previous_error) :ALEPrevious -error
nnoremap <silent> <Plug>(ale_previous_wrap) :ALEPreviousWrap
nnoremap <silent> <Plug>(ale_previous) :ALEPrevious
onoremap <silent> <Plug>(ale_show_completion_menu) <Nop>
vnoremap <silent> <Plug>(ale_show_completion_menu) <Nop>
nnoremap <silent> <Plug>(ale_show_completion_menu) :call ale#completion#RestoreCompletionOptions()
map <F5> bi{ea}
nnoremap <C-L> 
nnoremap <C-K> 
nnoremap <C-J> <NL>
nnoremap <C-H> 
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set autowriteall
set backspace=2
set expandtab
set fileencodings=utf-8,ucs-bom,default,latin1
set formatoptions=tcroql
set helplang=en
set ignorecase
set incsearch
set modelines=0
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/bundle/Vundle.vim,~/.vim/bundle/vim-fugitive,~/.vim/bundle/auto-pairs,~/.vim/bundle/ale,~/.vim/bundle/vim-python-pep8-indent,~/.vim/bundle/jellybeans.vim,~/.vim/bundle/vim-colors-solarized,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vimfiles/pack/dist-bundle/start/syntastic,/usr/share/vim/vimfiles/pack/dist-bundle/start/snippets,/usr/share/vim/vimfiles/pack/dist-bundle/start/puppet,/usr/share/vim/vimfiles/pack/dist-bundle/start/pathogen,/usr/share/vim/vimfiles/pack/dist-bundle/start/git-hub,/usr/share/vim/vim90,/usr/share/vim/vimfiles/pack/dist-bundle/start/puppet/after,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after,~/.vim/bundle/Vundle.vim,~/.vim/bundle/Vundle.vim/after,~/.vim/bundle/vim-fugitive/after,~/.vim/bundle/auto-pairs/after,~/.vim/bundle/ale/after,~/.vim/bundle/vim-python-pep8-indent/after,~/.vim/bundle/jellybeans.vim/after,~/.vim/bundle/vim-colors-solarized/after
set shiftwidth=4
set smarttab
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabstop=4
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Proj/python/sort_algorithms
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +0 .gitignore
argglobal
%argdel
$argadd .gitignore
edit .gitignore
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <C-P><C-E> =autopairs#AutoPairsIgnore()
inoremap <buffer> <silent> <C-P><C-S> :call autopairs#Keybinds#IgnoreInsertEnterCmd(":call autopairs#AutoPairsJump()")a
inoremap <buffer> <silent> <expr> <C-P><C-M> autopairs#AutoPairsToggleMultilineClose()
inoremap <buffer> <silent> <expr> <C-P><C-T> autopairs#AutoPairsToggle()
inoremap <buffer> <silent> <C-F> =autopairs#AutoPairsFastWrap()
inoremap <buffer> <silent> <C-P>' =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '''')
inoremap <buffer> <silent> <C-P>" =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '"')
inoremap <buffer> <silent> <C-P>} =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '}')
inoremap <buffer> <silent> <C-P>{ =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '{')
inoremap <buffer> <silent> <C-P>] =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', ']')
inoremap <buffer> <silent> <C-P>[ =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '[')
inoremap <buffer> <silent> <C-P>) =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', ')')
inoremap <buffer> <silent> <C-P>( =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '(')
noremap <buffer> <silent>  :call autopairs#AutoPairsJump()
noremap <buffer> <silent>  :call autopairs#AutoPairsToggleMultilineClose()
noremap <buffer> <silent>  :call autopairs#AutoPairsToggle()
noremap <buffer> <silent> <C-P><C-S> :call autopairs#AutoPairsJump()
noremap <buffer> <silent> <C-P><C-M> :call autopairs#AutoPairsToggleMultilineClose()
noremap <buffer> <silent> <C-P><C-T> :call autopairs#AutoPairsToggle()
inoremap <buffer> <silent>  =autopairs#AutoPairsFastWrap()
inoremap <buffer> <silent>  =autopairs#AutoPairsIgnore()
inoremap <buffer> <silent>  :call autopairs#Keybinds#IgnoreInsertEnterCmd(":call autopairs#AutoPairsJump()")a
inoremap <buffer> <silent> <expr>  autopairs#AutoPairsToggleMultilineClose()
inoremap <buffer> <silent> <expr>  autopairs#AutoPairsToggle()
inoremap <buffer> <silent> ' =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '''')
inoremap <buffer> <silent> " =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '"')
inoremap <buffer> <silent> } =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '}')
inoremap <buffer> <silent> { =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '{')
inoremap <buffer> <silent> ] =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', ']')
inoremap <buffer> <silent> [ =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '[')
inoremap <buffer> <silent> ) =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', ')')
inoremap <buffer> <silent> ( =autopairs#Keybinds#IgnoreInsertEnter('autopairs#AutoPairsMoveCharacter', '(')
inoremap <buffer> <silent>   =autopairs#AutoPairsSpace()
inoremap <buffer> <silent> " =autopairs#AutoPairsInsert('"')
inoremap <buffer> <silent> ' =autopairs#AutoPairsInsert('''')
inoremap <buffer> <silent> ( =autopairs#AutoPairsInsert('(')
inoremap <buffer> <silent> ) =autopairs#AutoPairsInsert(')')
inoremap <buffer> <silent> [ =autopairs#AutoPairsInsert('[')
inoremap <buffer> <silent> ] =autopairs#AutoPairsInsert(']')
inoremap <buffer> <silent> ` =autopairs#AutoPairsInsert('`')
inoremap <buffer> <silent> { =autopairs#AutoPairsInsert('{')
inoremap <buffer> <silent> } =autopairs#AutoPairsInsert('}')
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinscopedecls=public,protected,private
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=:#
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'gitignore'
setlocal filetype=gitignore
endif
setlocal fillchars=
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
set foldmarker=###,###
setlocal foldmarker=###,###
set foldmethod=marker
setlocal foldmethod=marker
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcroql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
set linebreak
setlocal linebreak
setlocal nolisp
setlocal lispoptions=
setlocal lispwords=
setlocal nolist
setlocal listchars=
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal nosmoothscroll
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'gitignore'
setlocal syntax=gitignore
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal thesaurusfunc=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal virtualedit=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
let s:l = 1 - ((0 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
set shortmess=filnxtToOS
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
