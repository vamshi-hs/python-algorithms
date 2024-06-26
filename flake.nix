{
	inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
	};
	outputs = {self,nixpkgs}: {
    defaultPackage.aarch64-linux = 
      with import nixpkgs {system = "aarch64-linux";};
      stdenv.mkDerivation {
        name = "python-algorithms";
	      src = self;
        buildInputs = [
          python3
        ];
	      nativeBuildInputs = [
          # pkgs.pkg-config		
          # pkgs.raylib
	      ];
	      # buildPhase  = ''
          	# gcc -Wall -Wextra -std=c11 `pkg-config --cflags raylib` -o hello ./src/main.c  `pkg-config --libs raylib`
	          # '';
	      # installPhase = ''
	             # mkdir -p $out/bin
               # install -t $out/bin hello
       # '';
      };
	};
}
