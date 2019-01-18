set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()  

Plugin 'VundleVim/Vundle.vim'
Plugin 'rafaqz/ranger.vim'
Plugin 'mkitt/tabline.vim'
Plugin 'davidhalter/jedi-vim'
Plugin 'Lokaltog/vim-powerline'
Plugin 'Nopik/vim-nerdtree-direnter'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'dhruvasagar/vim-table-mode'
Plugin 'junegunn/fzf'
Plugin 'plasticboy/vim-markdown'
Plugin 'Shougo/unite.vim'
Plugin 'majutsushi/tagbar'
Plugin 'rafaqz/citation.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'lifepillar/vim-mucomplete' 
Plugin 'tpope/vim-obsession'
Plugin 'tpope/vim-fugitive'
"Plugin 'jszakmeister/markdown2ctagsu'
"Plugin 'ajh17/VimCompletesMe'

call vundle#end()            " required
filetype plugin indent on    " required
"################################
" My SETUP                      #
"################################
	set autoread
  filetype on
	syntax on
	"set hidden
	"set history=100
	"filetype indent on
	"set nowrap
	set tabstop=2
	"set shiftwidth=2
	"set expandtab
	colorscheme elflord

  set nocursorline
" Change Color when entering Insert Mode
  autocmd InsertEnter * set cursorline 
  autocmd InsertLeave * set nocursorline

	set smartindent
	set autoindent
	set number
	set relativenumber
	set switchbuf=usetab,newtab
	"select all search results
	set hlsearch
	set ignorecase
" Splits open at the bottom and right, which is non-retarded, unlike vim defaults.
	set splitbelow
	set splitright

  highlight PmenuSel ctermfg=red  ctermbg=yellow

	let mapleader=" "
	map <leader>u :source ~/.vimrc<CR>
	noremap <leader>q :q<cr>
	set laststatus=2
"###########################################################
"PLUGINS SETTINGS                                          #
"###########################################################
"RANGER SETTINGS
"map <leader>rr :RangerEdit<cr>
"map <leader>rv :RangerVSplit<cr>
"map <leader>rs :RangerSplit<cr>
"map <leader>rt :RangerTab<cr>
"map <leader>ri :RangerInsert<cr>
"map <leader>ra :RangerAppend<cr>
"map <leader>rc :set operatorfunc=RangerChangeOperator<cr>g@

"VimCompletesMe - - - - - - - - - -
"settings:
"ENTER key to confirm choosen item
 
"mucomplete - - - - - - - - - - - - 
let g:mucomplete#enable_auto_at_startup = 1
set completeopt+=menuone
set completeopt+=noinsert
"let g:mucomplete#chains = { 'default' : ['incl', 'path', 'cmd', 'omni', 'ulti', 'file']  }





"PYTHON-YouCompleteMe------------
"  let g:ycm_server_python_interpreter='python2'
"SNIPS---------------------------
" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
"let g:UltiSnipsExpandTrigger="<Tab>"
"let g:UltiSnipsJumpForwardTrigger="<Tab>"
"let g:UltiSnipsJumpBackwardTrigger="<S-Tab>"
"let g:UltiSnipsListSnippets="<F12>"
"let g:UltiSnipsSnippetDirectories = ['~/.vim/UltiSnips', 'UltiSnips']
"let g:UltiSnipsUsePythonVersion = 3
"l If you want :UltiSnipsEdit to split your window.
"let g:UltiSnipsEditSplit="vertical"
"TableMode-----------------------
	let g:table_mode_corner="|"
	map <leader>tm :TableModeToggle<CR>
	"autocmd Filetype markdown let g:table_mode_always_active=1
	"autocmd Filetype markdown TableModeEnable
"TAGBAR-----------------------------------------------------
" 	- dodatek za programiranje
" 	- v desnem oknu odpre spremenljivke in funkcije
	nmap <F8> :TagbarToggle<CR>
	nmap <leader>e :TagbarOpenAutoClose<CR>
	let g:tagbar_autofocus = 1
	let g:tagbar_show_linenumbers = 2

"tagbar markdown language...................................
" Add support for markdown files in tagbar.
let g:tagbar_type_markdown = {
    \ 'ctagstype': 'markdown',
    \ 'ctagsbin' : '/home/david/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/markdown/markdown2ctags.py',
    \ 'ctagsargs' : '-f - --sort=no --sro=»',
    \ 'kinds' : [
        \ 's:sections',
        \ 'i:images'
    \ ],
    \ 'sro' : '»',
    \ 'kind2scope' : {
        \ 's' : 'section',
    \ },
    \ 'sort': 0,
\ }

"auto completition - drop down sugestion
let g:deoplete#enable_at_startup = 1

"SPELL CHECK
	map <F6> :set spell spelllang=
	map <S-F6> :set nospell<CR>
"-- next spell error
	nmap sn ]s
	nmap sp [s
"-- spell sugestions
	nmap ss z=
"vims' file search ----------------------------------------
	"set path+=**
	set wildmenu
	map fi :find *
"FZF--------------------------------------------------------
" 	- hitro iskanje filov
	let $FZF_DEFAULT_COMMAND = "find /home/david/ . -path '*/\.*' -type d -prune -o -type f -print -o -type l -print 2> /dev/null" 
	map ff :FZF<CR>
	let g:fzf_action = {
      \ 'enter': 'tab split',
      \ 'ctrl-x': 'split',
      \ 'ctrl-v': 'vsplit' }


"window-resize----------------------------------------------
	nnoremap <leader>h :vertical resize -15<CR>
	nnoremap <leader>l :vertical resize +15<CR>
	nnoremap <leader>j :resize +15<CR>
	nnoremap <leader>k :resize -15<CR>
"window open -----------------------------------------------
"--mogoče ne bom rabil odkar uporabljam RAnger plugin
	noremap <c-w>v :vnew<CR> 
"	noremap <c-w>n :new<CR> 

"NEERDTree - - - - - - - - - - - - - - - - - - - - - - - - - 
map <leader>r :NERDTreeToggle<CR>

"GIT--------------------------------------------------------
"instaliraj git-fugitive
	map <leader>gc :Gcommit -a<CR>==gi
	map <leader>gs :Gstatus<CR>
	map <leader>gu :Gpush<CR> :Gstatus<CR> :sleep 3<CR> :q<CR>
	map <leader>ga :Gpull<CR> :Gpush<CR> :Gstatus<CR> :sleep 3<CR> :q<CR>
	nnoremap <silent> <Esc> :nohlsearch<Bar>:echo<CR>
"map arrow keys
	map <Up> gk
	map <Down> gj
	map <ESC>oA <ESC>k
	map <ESC>oB <ESC>j
	map <ESC>oC <ESC>l
	map <ESC>oD <ESC>h
	nnoremap j gj
	nnoremap k gk
	
"move line UP/DOWN -----------------------------------------
  nnoremap <C-j> :m .+1<CR>==
	nnoremap <C-k> :m .-2<CR>==
	"inoremap <C-j> <Esc>:m .+1<CR>==gi
	"inoremap <C-k> <Esc>:m .-2<CR>==gi
	vnoremap <C-j> :m '>+1<CR>gv=gv
	vnoremap <C-k> :m '<-2<CR>gv=gv
" Shortcutting split navigation, saving a keypress:
"	map <C-h> <C-w>h
"	map <C-j> <C-w>j
"	map <C-k> <C-w>k
"	map <C-l> <C-w>l
	
"save => LEADER/CONTROL? + CRs
	nnoremap <leader>w :w<CR>
	inoremap <leader>w  <ESC>:w<CR>
"copy line
"nnoremap <C-c> :copy .<CR>
"	map <C-> "+P
	vnoremap <C-y> "+y
"	vnoremap y "+y
"new tab
	"nnoremap <C-t> :tabedit<CR>==gi
	nnoremap <C-t> :tabedit<CR>
"move trough tatbs (ze implementirano:)
" npr: 
" 2gt gre na 2 TAB
" plasticboy/markdown --------------------------------------   
	"map <leader>e :Toc<CR>
	let g:vim_markdown_toc_autofit = 1
"pandoc-----------------------------------------------------
	noremap <leader>s :!panzer -t revealjs -s -o %:p:r.html %:p -V revealjs-url=http://lab.hakim.se/reveal-js 
	noremap <leader>d :!pandoc --pdf-engine=xelatex % -o %:p:r.pdf 
	noremap <leader>p :w<CR>:!(clear && cd %:p:h && panzer %:p:t --to latex -o %:p:r.pdf --from markdown+hard_line_breaks --filter pandoc-citeproc --filter pandoc-mermaid --listings --pdf-engine=xelatex)<CR><CR>
	"noremap <C-p> :!zathura %:p:r.pdf <c-r> && disown <CR><CR>
  noremap <C-p> :!(zathura %:p:r.pdf & )<CR><CR>
"UNITE------------------------------------------------------
  nmap <space> [unite]
	nnoremap [unite] <nop>
	nmap <leader><leader> :Unite buffer<CR>
  
"CITATION---------------------------------------------------
	let g:citation_vim_bibtex_file="./bibtex.bib"
	let g:citation_vim_mode="bibtex"
	let g:citation_vim_cache_path='~/.vim/cache'
	let g:citation_vim_outer_prefix="["
	let g:citation_vim_inner_prefix="@"
	let g:citation_vim_suffix="]"
	nnoremap <leader>x :lcd %:p:h<CR> :!rm -f ~/.vim/cache/citation_vim_cache<CR> :Unite -buffer-name=citation-start-insert -default-action=append citation/key<CR><CR>
	autocmd Filetype markdown,rmd nnoremap <leader>b <Esc>:split %:p:h/bibtex.bib<CR><CR>
	
"MARKDOWN in EDITOR TEXTING BEHAVIOUR - - - - - - - - - - - - - - - - - - - 
	" to-do
	" inster TIMESHEET
	" premakni tako , da bodo insrti besedila delovali le v  INSERT MODEu!
	map ,n gg:-1r ! ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/markdown/markdown_header.sh<CR>gg
	map ,t :r !	~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/markdown/timesheetNotes.sh<CR>
	map ,h 0/<hh:mm><CR>"_c7l<CR><Esc>:-1r ! ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/markdown/insert_time.sh<CR>kJJ

	"---
	inoremap <Space><Tab> <Esc>/<++><Enter>"_c4l
	vnoremap <Space><Tab> <Esc>/<++><Enter>"_c4l
	map <Space><Tab> <Esc>/<++><Enter>"_c4l
	"---
	autocmd Filetype markdown,rmd inoremap ,n <Esc>gg:-1r ! ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/markdown/markdown_header.sh<CR>gg
	autocmd Filetype markdown,rmd inoremap ,t <++><Esc>:-1r ! ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/markdown/timesheetNotes.sh<CR>
	autocmd Filetype markdown,rmd inoremap ,h <CR><Esc>:-1r ! ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/markdown/insert_time.sh<CR>kJJi
	autocmd Filetype markdown,rmd inoremap ,b ****<++><Esc>F*hi
	autocmd Filetype markdown,rmd inoremap ,s ~~~~<++><Esc>F~hi
	autocmd Filetype markdown,rmd inoremap ,i **<++><Esc>F*i
	autocmd Filetype markdown,rmd inoremap ,l [](<++>)<++><Esc>F[a
  autocmd Filetype markdown,rmd inoremap ,p ```python<CR>```<CR><CR><esc>2kO
  autocmd Filetype markdown,rmd inoremap ,c ```cpp<cr>```<cr><cr><esc>2kO
	autocmd Filetype markdown,rmd inoremap ,j	![<++>\label{<++>}](./)<++><Esc>F/:Unite -input="*.jpg\|*.jpeg\|*.gif\|*.png\|*.bmp\|*.tiff" -default-action=append file_rec <CR> F[a 
	"autocmd Filetype markdown,rmd inoremap ,x <++><Esc>F<<Left><Left> <Esc>:!rm -f ~/.vim/cache/citation_vim_cache<CR> :Unite -buffer-name=citation-start-insert -default-action=append citation/key<CR><CR>
	autocmd Filetype markdown,rmd inoremap ,x <Esc>:!rm -f ~/.vim/cache/citation_vim_cache<CR> :Unite -buffer-name=citation-start-insert -default-action=append citation/key<CR><CR>
	"autocmd BufNew,BufRead markdown,*.md :setlocal textwidth=80
	"autocmd BufNew,BufRead markdown,*.md normal gggqG 
	autocmd BufRead markdown,*.md normal zR

	"auto wrapping selected text
	vnoremap ( xi ()<ESC>P2li
	vnoremap " xi ""<ESC>P2li
	vnoremap ' xi ''<ESC>P2li
	vnoremap [ xi []<ESC>P2li
	vnoremap { xi {}<ESC>P2li
	vnoremap < xi <><ESC>P2li

	set nocompatible
	if has("autocmd")
					filetype plugin indent on
	endif

"-----------------------------
"testing erea-----------------
"-----------------------------
"insert META-DATA
