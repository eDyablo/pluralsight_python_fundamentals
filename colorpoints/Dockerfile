FROM gcc AS build

WORKDIR /usr/src/colorpoints

COPY . .

RUN mkdir -p out \
    && g++ -std=c++20 *.cpp -o out/colorpoints -static -static-libgcc -static-libstdc++

FROM scratch

COPY --from=build /usr/src/colorpoints/out/colorpoints /usr/bin/colorpoints

ENTRYPOINT [ "/usr/bin/colorpoints" ]
