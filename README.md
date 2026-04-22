# Pretendard

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/orioncactus/pretendard/blob/HEAD/docs/images/thumbnail/dark/thumbnail.svg">
  <img src="https://github.com/orioncactus/pretendard/blob/HEAD/docs/images/thumbnail/light/thumbnail.svg" alt="Pretendard">
</picture>

Pretendard는 크로스 플랫폼에서 자연스럽게 보이며 다국어 타이포그래피에 적합한 현대적인 글꼴입니다. [Inter](https://github.com/rsms/inter), [본고딕](https://fonts.adobe.com/fonts/source-han-sans-korean), [M PLUS 1p](https://github.com/coz-m/MPLUS_FONTS)를 바탕으로 다듬어 9가지 굵기와 가변 글꼴을 제공합니다.

## 패키지

-   [Pretendard](/packages/pretendard/) — 표준 패밀리. 라틴·한글·일부 일본어 포함.
-   [Pretendard JP](/packages/pretendard-jp/) — 일본 환경용. 한국 한자 및 일본 한자 포함.
-   [Pretendard Std](/packages/pretendard-std/) — 한글 제외. 라틴·키릴 환경용 경량 버전.
-   [Pretendard GOV](/packages/pretendard-gov/) — 대한민국 공공 서비스 환경용.

자세한 사용법, OpenType 기능, 웹폰트 CDN 경로 등은 각 패키지의 README를 참고하세요.

## 빌드

`sources/` 의 Glyphs 소스에서 `fonts/` 로 폰트를 재생성하려면:

```bash
pip install -r requirements.txt
make build
```

Google Fonts 온보딩 규격([googlefonts-project-template](https://github.com/googlefonts/googlefonts-project-template))에 맞춰 구성되어 있으며, 패밀리별 `sources/config-*.yaml` 을 `gftools builder` 가 빌드합니다.

## 라이선스

[SIL Open Font License 1.1](/OFL.txt) 로 배포됩니다. 글꼴 단독 판매를 제외한 상업적 사용, 수정, 재배포가 가능합니다.
