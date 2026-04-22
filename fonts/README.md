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

현재 배포용 산출물은 `packages/<family>/dist/public/` 및 `packages/<family>/dist/web/` 경로에 위치하며, 이 디렉터리로의 매핑은 아래 작업에서 다룹니다. (Google Fonts 제출 시점에 바이너리가 이 위치에 존재해야 합니다.)

| 대상 | 기존 경로 | 이 디렉터리의 위치 |
| --- | --- | --- |
| OTF (static) | `packages/<family>/dist/public/static/*.otf` | `fonts/<Family>/otf/` |
| TTF (static) | `packages/<family>/dist/public/static/alternative/*.ttf` | `fonts/<Family>/ttf/` |
| Variable TTF | `packages/<family>/dist/public/variable/*.ttf` | `fonts/<Family>/variable/` |
| WOFF2 | `packages/<family>/dist/web/static/woff2/*.woff2` | `fonts/<Family>/webfonts/` |
