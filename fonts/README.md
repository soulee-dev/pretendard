# Fonts

이 디렉터리는 Google Fonts onboarding 규격에 맞춘 빌드 산출물의 배치 위치입니다. 각 패밀리는 아래 하위 디렉터리에 포맷별로 정리됩니다.

```
fonts/
├── Pretendard/
│   ├── otf/
│   ├── ttf/
│   ├── variable/
│   └── webfonts/
├── PretendardJP/
├── PretendardStd/
└── PretendardGOV/
```

바이너리는 루트 `Makefile`이 `sources/config-*.yaml`을 `gftools builder`로 돌려서 생성합니다.

```bash
make build
```

커밋되어 있는 현재 바이너리는 `packages/<family>/dist/`의 산출물을 한 차례 복사한 스냅샷입니다. 재생성 흐름(커맨드가 돌 때)은 `make build`가 담당하며, 결과는 `fonts/<Family>/{otf,ttf,variable,webfonts}`에 다시 쓰입니다.

| 포맷 | 생성 위치 |
| --- | --- |
| OTF (static) | `fonts/<Family>/otf/` |
| TTF (static) | `fonts/<Family>/ttf/` |
| Variable TTF | `fonts/<Family>/variable/` |
| WOFF2 | `fonts/<Family>/webfonts/` |

Pretendard Std는 `.glyphspackage` 없이 `scripts/refine/create-std.py`를 통해 Pretendard에서 파생되므로 `make build` 대상에 포함되지 않습니다.
