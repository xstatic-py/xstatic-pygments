for S in abap algol_nu algol arduino autumn borland bw colorful \
         default emacs friendly fruity igor lovelace manni monokai \
         murphy native pastie perldoc \
         rainbow_dash rrt sas stata tango trac vim vs xcode ; do
    pygmentize -f html -S $S > xstatic/pkg/pygments/data/css/$S.css
done


