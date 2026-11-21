# Phiếu QC 1 — Road v1.0 (bản kiểm sơ bộ)

**Lô được kiểm:** Tạ Đức Thắng — 2A202603163  
**Người kiểm:** Lê Việt Long — 2A202603043  
**Ngày:** 21/11/2026  
**Guideline:** Road v1.0  
**File được kiểm:** `taducthang-front.zip`, `taducthang-fisheye.zip`  
**Revision trong manifest:** 1  
**Số ảnh kiểm:** 6 (A01, A03, A05, B01, B06, B07)  
**Số nhãn trong 6 ảnh:** 55 (31 shape + 24 tag)

## Sáu ảnh được chọn

| Ảnh | Shape | Tag | Nhãn | Nhận xét XML                                        |
| --- | ----: | --: | ---: | --------------------------------------------------- |
| A01 |     9 |   4 |   13 | Có L1/R1; chưa kiểm độ lệch với ảnh                 |
| A03 |    10 |   4 |   14 | Có L1/R1; cờ occluded đều tắt, cần đối chiếu ảnh    |
| A05 |     2 |   4 |    6 | Không có lane; cần xác nhận có vạch nhìn thấy không |
| B01 |     4 |   4 |    8 | Không có lane; cần xác nhận với ảnh fisheye         |
| B06 |     3 |   4 |    7 | Lane position=other, phù hợp camera MVL             |
| B07 |     3 |   4 |    7 | Lane position=other, phù hợp camera MVR             |

## Tổng hợp theo mã

| Mã     | Loại lỗi                         |                               Số mục đã kiểm |                                          Số lỗi xác minh | Mức          |
| ------ | -------------------------------- | -------------------------------------------: | -------------------------------------------------------: | ------------ |
| QC1-01 | Tag camera                       |                                            6 |                                                        0 | nặng         |
| QC1-02 | Đủ L1/R1 nếu thấy vạch           |                                Chưa kiểm ảnh |                                            Chưa xác minh | nặng         |
| QC1-03 | Position                         | 2 lane ở B06/B07; còn lại chưa đối chiếu ảnh |                                   0 trong 2 mục kiểm XML | nặng         |
| QC1-04 | Tâm vạch / chiều / điểm dừng     |                         Chỉ kiểm chiều sơ bộ |                                   Chưa xác minh hình học | chính        |
| QC1-05 | Vạch đứt / che                   |                                Chưa kiểm ảnh |                                            Chưa xác minh | chính        |
| QC1-06 | Style / color / kind             |                      Kiểm cú pháp thuộc tính |                    0 lỗi cú pháp; chưa xác minh đúng ảnh | chính        |
| QC1-07 | Vùng lái                         |                                Chưa kiểm ảnh |                                            Chưa xác minh | chính        |
| QC1-08 | Đèn / màu                        |                                Chưa kiểm ảnh |                                            Chưa xác minh | nặng / chính |
| QC1-09 | Facing / type / group / biển phụ |                      Kiểm cú pháp thuộc tính |                         0 lỗi cú pháp; chưa xác minh ảnh | chính        |
| QC1-10 | Hình in / đủ biển                |                                Chưa kiểm ảnh |                                            Chưa xác minh | chính        |
| QC1-11 | Fisheye                          |                    2 lane B06/B07 (position) | 0 lỗi position trong 2 lane; phần hình học chưa xác minh | chính        |
| QC1-12 | File                             |                                        2 ZIP |                                        0 lỗi đọc ZIP/XML | nhẹ / nặng   |

## Danh sách lỗi

Qua kiểm tra cấu trúc XML của 6 ảnh được chọn, chưa xác nhận được lỗi về định dạng hoặc giá trị thuộc tính. Tuy nhiên, có ba trường hợp cần đối chiếu trực tiếp với ảnh gốc trước khi kết luận:

| # | Mã nghi vấn | Ảnh | Nhãn | Mức dự kiến nếu xác nhận | Mô tả |
|---|---|---|---|---|---|
| 1 | QC1-05 | A03 | lane | Chính | Cần kiểm tra đoạn vạch bị che và việc sử dụng cờ `occluded`. |
| 2 | QC1-02 | A05 | lane | Nặng | Không có nhãn lane trong XML; cần xác định ảnh có vạch L1/R1 nhìn thấy được hay không. |
| 3 | QC1-02 | B01 | lane | Nặng | Không có nhãn lane trong XML; cần xác định ảnh có vạch làn nhìn thấy được hay không. |

## Ca cần xem ảnh / hỏi coach

| Ảnh | Câu hỏi cho lead                                | Lời đáp |
| --- | ----------------------------------------------- | ------- |
| A05 | Có thấy vạch L1/R1 không?                       |         |
| A03 | Đoạn vạch bị che có cần bật occluded không?     |         |
| B01 | Không có lane có phù hợp ảnh fisheye này không? |         |

## Quyết định (tạm thời)

- **Lỗi nặng:** 0; chưa kiểm đủ dấu hiệu hình ảnh
- **Lỗi chính:** Chưa xác định; không tính tỉ lệ % cho đến khi hoàn thành QC trực quan
- **Lỗi nhẹ:** label các nhãn chưa chuẩn
- **Ca chờ lead:**
- **Quyết định tạm thời:** Hold
- **Lý do:** Qua kiểm tra dữ liệu nhãn của 6 ảnh được chọn, các file có thể đọc được và các thuộc tính được kiểm tra có giá trị hợp lệ. Tuy nhiên, một số trường hợp cần đối chiếu trực tiếp với ảnh gốc để xác định việc thiếu nhãn lane hoặc xử lý đoạn bị che khuất có đúng guideline Road v1.0 hay không. Do chưa đủ căn cứ để kết luận chất lượng toàn bộ mẫu kiểm, lô được tạm giữ ở trạng thái Hold để xác minh trước khi quyết định Release hoặc Rework.
