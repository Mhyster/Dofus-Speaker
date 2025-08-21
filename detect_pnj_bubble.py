def detect_pnj_bubble(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    h, w = gray.shape
    candidates = []

    for c in contours:
        x, y, ww, hh = cv2.boundingRect(c)
        area = ww * hh
        if area > 0.02*w*h and ww/hh > 2:  # zone large
            candidates.append((x,y,ww,hh))

    if not candidates:
        return frame

    # Trier par position verticale
    candidates.sort(key=lambda r: r[1])
    x,y,ww,hh = candidates[0]  # bulle PNJ

    # 🔥 Ajustement : on remonte de 100 pixels (sans dépasser le haut)
    y = max(0, y - 100)
    hh = hh + 100

    return frame[y:y+hh, x:x+ww]
