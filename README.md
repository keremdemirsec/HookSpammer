# Discord Webhook İşlem Projesi

Bu proje, Discord'da webhookları spamlayan ve silen bir Python programını içerir. Kullanıcıya basit bir arayüz sunar ve belirtilen webhook URL'sine sürekli mesajlar gönderme veya webhookları silme gibi işlemleri gerçekleştirebilir.

## Açıklama

Bu Python programı, kullanıcı tarafından belirtilen Discord webhook URL'sine sürekli mesajlar gönderme veya webhookları silme gibi işlemleri gerçekleştirir. Program, basit bir arayüzle kullanıcıya seçenekler sunar ve kullanıcı dostu bir deneyim sağlar.

## Başlangıç

Projenin yerel bir kopyasını almak ve çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

Projenin çalışması için aşağıdaki yazılımlara ihtiyaç vardır:

- Python 3
- requests kütüphanesi
- colorama kütüphanesi

### Kurulum

1. Bu depoyu klonlayın:

    ```bash
    git clone https://github.com/keremdemirsec/HookSpammer
    ```

2. Proje klasörüne gidin:

    ```bash
    cd HookSpammer
    ```

3. Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

4. Uygulamayı çalıştırın:

    ```bash
    python main.py
    ```

## Kullanım

Programı çalıştırdığınızda, kullanabileceğiniz komut satırı seçenekleri şunlardır:
- `--webhook`: Discord webhook URL'sini belirtmek için kullanılır.
- `--islem`: Yapılacak işlemi belirtmek için kullanılır (`spam` veya `sil`).
- `--mesaj`: Spam işlemi için gönderilecek mesajı belirtmek için kullanılır (opsiyonel).

Örnek kullanım:

```bash
python main.py --webhook WEBHOOK_ADRESI --islem spam --mesaj "Selamlar"
python main.py --webhook WEBHOOK_ADRESI --islem sil
```

## Katkıda Bulunma

Eğer projeye katkıda bulunmak istiyorsanız, lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Detaylar için lisans dosyasını inceleyin.

## İletişim

Eğer sorularınız, önerileriniz veya geri bildirimleriniz varsa, bana [e-posta](mailto:keremdemirsec@email.com) üzerinden ulaşabilirsiniz.
