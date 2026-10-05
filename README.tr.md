# receipts 🧾

[![Validate skills](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml)
[![Latest release](https://img.shields.io/github/v/release/effectustasi/agent-receipts)](https://github.com/effectustasi/agent-receipts/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#kurulum)
[![GitHub stars](https://img.shields.io/github/stars/effectustasi/agent-receipts?style=social)](https://github.com/effectustasi/agent-receipts/stargazers)

[English](README.md) · **Türkçe**

**Kodlama agent'ın "Bitti ✅" diyor. Kodu hiç çalıştırmadı.**

`receipts`, Claude Code, Codex, Cursor ve benzeri agent'ların bir şey iddia etmeden önce **kanıt göstermesini** sağlayan bir skill paketi.

## Öncesi / sonrası

**receipts olmadan**

> Tarih ayrıştırıcıyı ISO hafta formatını destekleyecek şekilde güncelledim. Artık çalışması lazım. Bitti ✅

**receipts ile**

> Bitti. Makbuz:
> ```
> $ pytest tests/test_dates.py
> 7 passed in 0.38s
> ```

ya da kontrol edemediğinde:

> `parse_date` artık ISO haftalarını kabul ediyor. **Doğrulanmadı**: burada test ortamı kurulu değil.
> Kontrol için: `python -c "from app.dates import parse_date; print(parse_date('2026-W40'))"`

## Skill'ler

| Skill | Agent'ını şundan alıkoyar |
|---|---|
| [`prove-it`](skills/prove-it/SKILL.md) | Hiçbir şey çalıştırmadan "bitti", "düzeldi", "testler geçti" demek |
| [`no-guessing`](skills/no-guessing/SKILL.md) | Fonksiyon adlarını, CLI parametrelerini, ayar anahtarlarını ezberden uydurmak |
| [`repro-first`](skills/repro-first/SKILL.md) | Hiç bozulduğunu görmediği hataları "düzeltmek" |

## Kurulum

**Claude Code**

```
/plugin marketplace add effectustasi/agent-receipts
/plugin install receipts@receipts
```

### Codex CLI

Codex CLI işe başlamadan önce `AGENTS.md` dosyasını okur. Proje kök dizininde receipts skill'lerini bu dosyaya ekle:

```bash
for skill in prove-it no-guessing repro-first; do
  curl -fsSL "https://raw.githubusercontent.com/effectustasi/agent-receipts/main/skills/$skill/SKILL.md" >> AGENTS.md
done
```

Skill'leri tüm projelerde kullanmak için bunun yerine `~/.codex/AGENTS.md` dosyasına ekle. Dosyayı değiştirdikten sonra yeni bir Codex oturumu başlat ve aktif talimatları özetlemesini iste:

```bash
codex --ask-for-approval never "Summarize the current instructions."
```

Arama sırası, genel ve proje kapsamı ile geçersiz kılmalar için [resmi Codex talimat belgelerine](https://developers.openai.com/codex/agent-configuration/agents-md) bak.

**Diğer agent'lar** (Cursor, Copilot, Gemini CLI, OpenCode…)

Skill klasörlerini agent'ının skill dizinine kopyala ya da her `SKILL.md` dosyasının içeriğini `AGENTS.md` veya kurallar dosyana yapıştır.
Agent'a özel kurulum rehberleri katkıya açık: [`agent-support`](https://github.com/effectustasi/agent-receipts/labels/agent-support) etiketli issue'lardan agent'ını seç.

## Benchmark

Aynı görevler `receipts` ile ve onsuz çalıştırılıyor; agent'ın gerçek olmayan bir başarıyı ne sıklıkla iddia ettiği ölçülüyor. Her çalıştırmayı agent değil, bir script kontrol ediyor.

Şimdiye kadarki sonuçlar (Claude Code, 225 çalıştırma): Sonnet 5.5 hiçbir kurulumda yanlış başarı iddia etmedi. Haiku 4.5 receipts olmadan 30 çalıştırmanın 13'ünde etti ve receipts bunu henüz güvenilir şekilde azaltmıyor: Haiku skill'leri kendiliğinden nadiren açıyor. Skill'ler `CLAUDE.md`'deyken testleri geçsin diye değiştirmeyi bıraktı ve bunun yerine sordu.
Tablolar, kayıtlar ve nasıl çalıştırılacağı: [benchmark/](benchmark/README.md). Yeni görevlere açığız, [`benchmark`](https://github.com/effectustasi/agent-receipts/labels/benchmark) etiketine bak.

## Katkı

Yeni skill'ler, çeviriler, diğer agent'lar için kurulum rehberleri ve benchmark görevleri memnuniyetle karşılanır. [CONTRIBUTING.md](CONTRIBUTING.md) ve [`good first issue`](https://github.com/effectustasi/agent-receipts/labels/good%20first%20issue) etiketiyle başla.

## Lisans

MIT

## effectustasi'nin diğer araçları

- [blender-dlss5-neural-rendering](https://github.com/effectustasi/blender-dlss5-neural-rendering): Blender viewport'u ve render'ları DLSS 5 nöral render ile
- [metahuman-face-capture](https://github.com/effectustasi/metahuman-face-capture): Blender'da webcam ile MetaHuman yüz yakalama
- [autodesk-inventor-mcp](https://github.com/effectustasi/autodesk-inventor-mcp): AI agent'ları açık bir Autodesk Inventor oturumuna bağla
- [unreal-groom-alembic-exporter](https://github.com/effectustasi/unreal-groom-alembic-exporter): UE Groom asset'lerini (MetaHuman saçı) Alembic'e aktar
