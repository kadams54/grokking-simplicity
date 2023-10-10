(def computed
  (->>
    (range 1 8)
    (filter even?)
    (map (fn [n] (repeat n n)))
    (reduce concat)))

(print computed)
