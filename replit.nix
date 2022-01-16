{ pkgs }: {
    deps = [
        pkgs.cowsay
        pkgs.python39
        pkgs.python39Packages.pip
        pkgs.nodejs-16_x
    ];
}