# Báo cáo cá nhân — Ngày 11

Họ tên: Lê Việt Long · Mã học viên: `2A202603043`  
Phiên bản CVAT (Help → About): Chưa xác minh, cần ảnh Help → About.  
Guideline: Road v1.0 · Lần nộp (`revision` trong manifest): 1.  
Thời điểm export theo trường `meta/dumped` trong XML: 21/11/2026, 15:41:51 (giờ Việt Nam). Thời điểm trên giao diện CVAT chưa đối chiếu.  
Số lần nộp lại sau Rework: Chưa xác minh. Manifest ghi lần nộp 1 và chưa có phiếu QC nhận được để đối chiếu.

## 1. Kiểm project

| Mục | Đúng như guideline Road v1.0? | Ghi chú |
| --- | --- | --- |
| 6 label, đúng kiểu | Khớp trong metadata và các shape của hai XML | Polyline gồm `lane`, `road_curb`. Polygon gồm `crosswalk`, `drivable`. Rectangle gồm `traffic_light`, `traffic_sign` (ghi là `box` trong XML). |
| Thuộc tính và giá trị | Khớp trong XML | Cả 279 shape có đủ thuộc tính theo label và giá trị hợp lệ. Độ chính xác của giá trị theo nội dung ảnh chỉ được rà ở các ca nêu trong mục 3. |
| 4 tag ảnh | Đủ và đúng cấu trúc trong cả 28 ảnh | Mỗi ảnh có đúng một `camera`, `timeofday`, `weather`, `source`, mỗi tag có một thuộc tính select `value` hợp lệ. Tất cả tag `camera` khớp nhóm A hoặc hậu tố WoodScape. |

| Label | Thuộc tính và giá trị theo Road v1.0 |
| --- | --- |
| `lane` | `position` = L1, R1, L2, R2, other. `style` = solid, dashed. `color` = white, yellow, other. `kind` = single, double. Dùng cờ có sẵn `occluded` khi nối qua đoạn bị che. |
| `road_curb`, `crosswalk` | Không có thuộc tính riêng. |
| `drivable` | `area_type` = direct, alternative. |
| `traffic_light` | `color` = red, yellow, green, off, unknown. `type` = vehicle, pedestrian, beacon. `facing` = front, side, back. `edge_zone` là ô tick, nhận true hoặc false. |
| `traffic_sign` | `group` = prohibitory, mandatory, warning, information, supplementary, other. `facing` = front, side, back. `edge_zone` là ô tick, nhận true hoặc false. |
| `camera` | `value` = front, fisheye_front, fisheye_rear, fisheye_left, fisheye_right. |
| `timeofday` | `value` = day, dusk, night. |
| `weather` | `value` = clear, overcast, rain, fog, other. |
| `source` | `value` = real, simulated. |

Cách kết thúc polyline theo hướng dẫn CVAT của lớp: chọn **Polyline → label → Shape**, đặt điểm từ gần xe ra xa rồi nhấn **N**. Cách đặt tag ảnh: chọn công cụ **Tag**, đặt `camera` trước rồi đến `timeofday`, `weather` và `source`. Mở **Objects → Details** để kiểm tra `value` của từng tag. Chưa xác minh thao tác trên phiên bản CVAT của bài nộp. [Hướng dẫn thao tác CVAT](docs/huong_dan_cvat_bang_hinh.md)

XML cho biết dữ liệu thuộc job 17. Trạng thái project và trạng thái `completed` của job chưa xác minh, cần xem trực tiếp trên CVAT.

## 2. Số lượng đã gán

| Task | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| front (A01–A12) | 12 | 32 | 13 | 10 | 24 | 35 | 45 |
| front-extra (A13–A16, đã làm 4 / 4) | 4 | 12 | 0 | 6 | 9 | 13 | 20 |
| fisheye (B01–B08) | 8 | 6 | 9 | 9 | 10 | 7 | 6 |
| fisheye-extra (B09–B12, đã làm 4 / 4) | 4 | 0 | 3 | 5 | 4 | 1 | 0 |
| **Tổng** | **28** | **50** | **25** | **30** | **47** | **56** | **71** |

Đếm trực tiếp các phần tử hình học dưới từng `<image>`. Bốn nhóm theo mã ảnh có lần lượt 159, 60, 47 và 13 shape, cộng lại **279**, khớp tổng của hai ZIP (219 front và 60 fisheye). Có thêm **112 tag**, tính riêng. Cả 28 ảnh đều có ít nhất một shape. Tên ảnh trùng với bộ ảnh cục bộ trong `data/`.

## 3. Bảng ca khó

| Ảnh | Nhãn | Phân vân giữa | Đã chọn | Lý do |
| --- | --- | --- | --- | --- |
| A04 | `lane` | Ba polyline cùng R1 (QC1-05) có thể là các đoạn của một vạch hoặc các ranh khác nhau. | XML gán một R1 trắng đứt phía trong và hai R1 trắng liền phía ngoài. Ảnh gốc cho thấy hai nét liền nằm sát dải xanh, tách khỏi vạch đứt. | Vạch đứt sát bên phải làn hiện tại. Hai nét ngoài nằm ở ranh xa hơn nên việc gán cả ba là R1 cần rà lại. |
| A05 | `lane`, `road_curb` | Thiếu L1/R1 (QC1-02) hoặc đường không có vạch làn nhìn thấy. | XML không có `lane`, có một `road_curb` và một `drivable`. Khi xem ảnh gốc, không thấy vạch phân làn rõ trên phần đường giữa hai hàng xe đỗ. | Chỉ gán vạch sơn nhìn thấy. Cần coach xác nhận ngoại lệ QC1-02 và ghi lý do vào phiếu. |
| A06 | `lane`, `road_curb`, `crosswalk` | Thiếu R1 (QC1-02) hoặc ranh phải nằm ở mép đường cạnh cột. | XML có L1, hai `road_curb` và một `crosswalk`. Có nét trắng ngoài cùng bên phải ảnh, nhưng chưa rõ có phải ranh của làn xe mình. | Vạch ngựa vằn và mép không sơn có nhãn riêng. Cần đối chiếu ảnh gốc ở vùng bên phải cột với coach để xác định R1 hoặc xin xác nhận ngoại lệ. |
| A09 | `lane` | Thiếu R1 (QC1-02) và hai polyline L2 (QC1-05). | XML gán vạch trắng đứt là L1 và gán hai nét trắng liền là hai L2, cả hai đều có `kind=double`. Ảnh gốc cho thấy hai nét liền song song bên trái và vạch đứt bên phải làn xe mình. | Đối chiếu ảnh và tọa độ cho thấy cặp vạch trái được vẽ thành hai shape dù cùng là một vạch đôi. Vạch đứt đã có shape nên cần rà lại `position` của các shape hiện có. |
| B02 | `traffic_light` | Hai hộp gần góc trên phải có cần bật `edge_zone` (QC1-11) hay không. | XML ghi `false` cho cả hai. Tâm hộp cách tâm ảnh 591,78 px và 629,38 px theo phép tính của lint. | Ảnh gốc cho thấy hai hộp ở vùng rìa. Cả hai vượt ngưỡng 512 px theo cách lấy bán kính của lint và cần kiểm lại cờ theo vòng ảnh. |
| B03 | `traffic_sign` | Hộp biển cấm bên trái có cần bật `edge_zone` (QC1-11) hay không. | XML ghi `true` cho hộp bắt đầu ở (172,72, 299,46). Tâm hộp cách tâm ảnh 486,94 px theo phép tính của lint. | Tâm hộp nằm trong ngưỡng 512 px theo cách tính của lint. Cần đối chiếu vị trí với vòng ảnh trước khi chốt cờ. |
| B08 | `road_curb` | Đoạn hai điểm (QC1-11) là một mép riêng hay đoạn trùng. | XML có một polyline hai điểm với đúng cặp tọa độ liên tiếp trong polyline 10 điểm. Ảnh gốc cho thấy một mép đường ở đoạn này. | Đoạn chồng trùng xác minh được từ XML. Polyline theo cung của mép đường fisheye cần các điểm trung gian ở chỗ cong. |

| Mã lint | Nặng | Chính | Nhẹ | Nội dung |
| --- | ---: | ---: | ---: | --- |
| QC1-02 | 4 | 0 | 0 | A05 thiếu L1 và R1, A06 thiếu R1, A09 thiếu R1. |
| QC1-05 | 0 | 2 | 0 | A04 có ba R1 và A09 có hai L2. |
| QC1-08 | 0 | 0 | 8 | Hộp đèn thấp hơn 8 px ở A03 (2), A04 (2), A15 (2), A16 (2). |
| QC1-10 | 0 | 0 | 7 | Hộp biển thấp hơn 8 px ở A04 (1), A10 (4), A15 (2). |
| QC1-11 | 0 | 4 | 0 | B02 có hai gợi ý bật `edge_zone`, B03 có một gợi ý tắt, B08 có một `road_curb` hai điểm. |
| **Tổng** | **4** | **6** | **15** | **25 cảnh báo trên 28 ảnh.** |

Các mức trong bảng là mức do `lint` in ra. Kiểm tra trực quan ở trên chỉ áp dụng cho các ca nêu trong bảng ca khó. Chưa có Ground Truth hợp lệ của coach để chạy `road_check check`. Hộp dưới 8 px là gợi ý tự kiểm vì guideline chỉ bắt buộc gán đối tượng từ 8 px trở lên. [Guideline Road v1.0](docs/guideline_road_v1.0.md) · [Thang mức lỗi QC 1](docs/qc_severity_road_v1.0.md)

## 4. Phiếu QC 1 nhận được

Bạn kiểm lô của tôi: Chưa xác minh.  
Quyết định nhận được: Chưa nhận phiếu QC từ học viên kiểm.

| Mã lỗi | Số lỗi | Đồng ý? | Đã sửa? |
| --- | ---: | --- | --- |
| Chưa có phiếu nhận được | — | Chưa có căn cứ phản hồi | Chưa xác minh |

Phiếu hiện có do tôi lập để kiểm lô của Tạ Đức Thắng. Repo chưa có bản riêng mang tên file theo checklist nộp bài. [Phiếu QC 1 cho Tạ Đức Thắng](templates/qc1_form.md)

## 5. Kiểm file export

| File | Mở lại được? | Số shape ảnh 1 (job / file) | Số shape ảnh 2 (job / file) | Tag camera có trong XML? |
| --- | --- | --- | --- | --- |
| `levietlong-front.zip` | Có, ZIP qua kiểm tra CRC, XML 1.1 đọc được và lint chạy xong | Job 17 / A01: 9 | Job 17 / A08: 28 | Có, 16/16 là `front`. |
| `levietlong-fisheye.zip` | Có, ZIP qua kiểm tra CRC, XML 1.1 đọc được và lint chạy xong | Job 17 / B03: 12 | Job 17 / B08: 7 | Có, 12/12 khớp hậu tố. B03 là `fisheye_rear`, B08 là `fisheye_right`. |

Hai ZIP được tách bằng `split_cvat.py` từ export `levietlong-all.zip` của một task CVAT gồm 28 ảnh. Đã đối chiếu từng ảnh với export gốc. Tên và phần tử nhãn khớp, ID ảnh được đánh lại theo mỗi ZIP. Metadata trong cả hai ZIP vẫn ghi job gốc 17 với 28 ảnh. Bốn nhóm ở mục 2 là nhóm logic theo mã ảnh. Chưa xác minh việc nhập lại lên CVAT.

Manifest `road-delivery/1`, revision **1**, được tạo lúc **2026-11-21 08:43:31 UTC** (**15:43:31 giờ Việt Nam**). Mỗi ZIP chỉ chứa `annotations.xml`, khớp `contains_images=false`. Số ảnh, số ảnh đủ tag, số shape theo label, số byte, SHA-256 và tổng cảnh báo lint đều khớp. [Manifest bàn giao](levietlong-manifest.json)

| ZIP | Số byte | SHA-256 đối chiếu |
| --- | ---: | --- |
| front | 16.503 | `404e8cd6930b41e2712971095fc0fef51ac4bff1f6d3e071ca3259078e1bbb71` |
| fisheye | 10.192 | `9535f85dc62dfb7af11d20ccfac407cbd91821a4bb0ca5a80598ea7b02` |

Đã chạy `PYTHONPATH=src python -m road_lab.road_check lint levietlong-front.zip levietlong-fisheye.zip` với đầu ra UTF-8. Checklist trước khi nộp còn mục `completed` chưa xác minh, bốn cảnh báo mức nặng QC1-02 chưa xử lý hoặc có xác nhận ngoại lệ, và ba ảnh chụp CVAT chưa có. [Checklist nộp bài](SUBMISSION.md)

## 6. Ảnh chụp màn hình

Repo có ảnh minh họa CVAT của tài liệu lab. Chưa tìm thấy ảnh chụp CVAT của bài này trong repo. [Thư mục và hướng dẫn bổ sung minh chứng](evidence/README.md)

1. **Tab Labels của project:** Chưa có. Cần ảnh thấy sáu label và bốn tag.
2. **Một ảnh camera trước đã gán đủ:** Chưa có. Có thể chụp A08 đang mở trên CVAT với lớp nhãn hiển thị.
3. **Một ảnh fisheye có polyline cong:** Chưa có. Có thể chụp B03 và phóng to đoạn cong để thấy các đỉnh.
4. **Đoạn XML thật có `<polyline label="lane">`:** Trích A01 trong `annotations.xml` của `levietlong-front.zip`. Tọa độ giữ nguyên.

   ```xml
   <polyline label="lane" source="manual" occluded="0" points="107.64,719.87;282.66,572.04;316.27,544.86;343.12,521.85;353.53,513.50" z_order="0">
     <attribute name="position">L1</attribute>
     <attribute name="style">dashed</attribute>
     <attribute name="color">white</attribute>
     <attribute name="kind">single</attribute>
   </polyline>
   ```

## 7. Tự đánh giá

QC1-02 là cảnh báo mức nặng lặp nhiều nhất. A05 cho thấy cần nhìn lại ảnh trước khi quyết định có thiếu vạch hay không. Ở A09, vạch đứt đã được vẽ nhưng `position` cần rà lại. B08 có một đoạn mép đường trùng tọa độ, kiểm được trực tiếp trong XML. Sang Ngày 20, tôi sẽ xác định ranh hai bên làn xe trước khi đặt `position`, rồi kiểm các đường trùng và phóng to những đoạn cong của ảnh fisheye trước khi export.

Polyline tạo đích vị trí cho mô hình phát hiện làn. Nếu đặt sai `position` như ca cần rà ở A09, mô hình có thể học nhầm vạch thuộc phía nào của làn xe. Nếu vẽ một vạch thành nhiều đoạn, quá trình tạo đích theo hàng neo có thể đánh dấu nhầm các hàng ở khoảng hở là không có làn. Chưa có bằng chứng các ca này đã được sửa trong bản export hiện tại.

## 8. (Tùy chọn, buffer) Từ polyline đến đích row-anchor

| y | 720 | 680 | 640 | 600 | 560 |
| --- | ---: | ---: | ---: | ---: | ---: |
| x của chúng tôi | — | — | — | — | — |
| x của bạn kia | — | — | — | — | — |

Chưa thực hiện phần tùy chọn vì chưa có dữ liệu row-anchor của hai học viên trên cùng một ảnh.

1. Hàng đổi thành “không có làn” khi dừng polyline sớm 40 px: chưa tính.
2. Chênh lệch ở hàng 720 và 560, và ảnh hưởng đến LKA: chưa so sánh.
3. Ảnh hưởng của việc đảo chiều polyline đến phép tính và script: chưa thực hiện.
