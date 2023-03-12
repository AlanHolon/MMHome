\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{matemaj}[2022/12/08 MateMajorana class]
%\RequirePackage{HoQuests}
%\RequirePackage{xcolor}
\def\@pagine{gobble}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\DeclareOption{pag}{\def\@pagine{arabic}}
\DeclareOption{a5}{\def\AVvero{\relax}}
\DeclareOption{colors}{\let\qst@color\color}
\ProcessOptions\relax
\LoadClass[a4paper]{report}
%
\ifx\AVvero\undefined\else
   \newlength{\AVlarg}%
   \setlength{\AVlarg}{\dimexpr\pdfpageheight/2}%
   \setlength{\pdfpageheight}{\pdfpagewidth}%
   \setlength{\pdfpagewidth}{\AVlarg}%   
\fi
%\pdfpagewidth 8.27in
%\pdfpageheight 11.69in
\headheight 0pt
\headsep 0pt
\footskip 0in
\marginparwidth 0pt
\marginparsep 0pt
\oddsidemargin \dimexpr 0.5in -1in
\evensidemargin \dimexpr 0.5in -1in
\topmargin \dimexpr 0.3in -1in
\textwidth \dimexpr \pdfpagewidth -2\oddsidemargin -2.1in
\textheight \dimexpr \pdfpageheight -2\topmargin -2in
\columnsep 60pt%
\setlength{\parindent}{0pt}
\setlength{\parskip}{1em plus .2em minus .2em}
\pagenumbering{\@pagine}%
\newcounter{cont@@qst0}
\setcounter{cont@@qst0}{0}%

%\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tikz}
%\usetikzlibrary{patterns}
%\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\setlength\parskip{0.5em}
\newlength{\dqst}
\dqst=.5cm

\def\quesito#1[#2;#3]#4\par{\vspace{\dqst}\hrule\stepcounter{cont@@qst0}{\bf Quesito \arabic{cont@@qst0}}\hfill Intervallo della risposta: [ #2 ; #3 ]\\[-8pt]\hrule#4\\[-8pt]\hrule\vspace{\dqst}}

\def\quesitotc#1[#2;#3] [#4]#5[#6]#7\par{\vspace{\dqst}\hrule\stepcounter{cont@@qst0}{\bf Quesito \arabic{cont@@qst0}}\hfill Intervallo della risposta: [ #2 ; #3 ]\\[-8pt]\hrule\begin{minipage}[t]{#4\textwidth}#5\end{minipage}\begin{minipage}[t]{#6\textwidth}#7\end{minipage}\\[6pt]\hrule\vspace{\dqst}}

\def\sec#1{\par{\bf\large#1}\par}
\def\titolo#1\par{\par\begin{center}\bf\Large#1\end{center}\par}
\def\tikspace{$ $\vspace{-.3cm}\\\hspace*{1cm}}
\def\btn#1{\begin{tikzpicture}
\draw (0,0) rectangle (.6,.6) node[pos=.5] {$#1$};
\end{tikzpicture}}
