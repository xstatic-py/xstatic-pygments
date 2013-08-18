for S in monokai manni rrt perldoc borland colorful default murphy vs trac tango fruity autumn bw emacs vim pastie friendly native; do
    pygmentize -f html -S $S > xstatic/pkg/pygments/data/css/$S.css
done

