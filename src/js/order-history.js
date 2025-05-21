// const orderData = {
//   "جاری ۲": [
//     "<div class='order-card-inner'>سفارش جاری ۱</div>",
//     "<div class='order-card-inner'>سفارش جاری ۲</div>"
//   ],
//   "تحویل شده ۲۶": [
//     "<div class='order-card-inner'>تحویل شده ۱</div>",
//     "<div class='order-card-inner'>تحویل شده ۲</div>"
//   ],
//   "مرجوع شده ۴": [
//     "<div class='order-card-inner'>مرجوعی ۱</div>",
//     "<div class='order-card-inner'>مرجوعی ۲</div>"
//   ],
//   "لغو شده ۴": [
//     "<div class='order-card-inner'>لغو شده ۱</div>",
//     "<div class='order-card-inner'>لغو شده ۲</div>"
//   ]
// };

const tabCache = {
  "تحویل شده ۲۶": document.getElementById('orders-container').innerHTML
};

// function change(button) {
//   // حذف کلاس active از همه دکمه‌ها
//   document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));

//   // افزودن active به دکمه‌ی فعلی
//   button.classList.add('active');

//   // گرفتن متن تب
//   const tabName = button.textContent.trim();

//   // دریافت محتوای دو کارت از آبجکت
//   const [html1, html2] = orderData[tabName];

//   // جایگزینی در دو کارت
//   document.getElementById('card1').innerHTML = html1;
//   document.getElementById('card2').innerHTML = html2;
// }

function change(button) {
  const tabName = button.textContent.trim();
  const container = document.getElementById('orders-container');

  // حذف کلاس active از دکمه‌ها
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  button.classList.add('active');

  // اگه محتوای این تب توی cache نیست، تولیدش کن (اینجا به صورت ساده دستی می‌ذاریم)
  if (!tabCache[tabName]) {
    if (tabName === "جاری ۲") {
      tabCache[tabName] = `
        <div class="no-order" id="no-order-yet">
  <p class="body-2">سفارش جاری وجود ندارد.</p>
  <img src="../src/images/user-profile-images/order-history/Illustration.svg" alt="404img"/>
</div>
      `;
    } else if (tabName === "مرجوع شده ۴") {
      tabCache[tabName] = `
         <div class="rejected-item">
      <div class="reject-container">
        <div class="inner-container">
          <div class="reject-header">
            <span class="date">۳ شهریور ۱۴۰۲</span>
            <span class="tracking-code">کد پیگیری مرجوعی: ۳۵۴۵۳۴۵۲۱</span>
          </div>

          <div class="reject-card">
            <div class="reject-card-header">
              <img
                src="../src/images/user-profile-images/order-history/reject-icon.svg"
                alt="آیکن بستن"
                class="reject-icon-close"
              />
              <span class="rejected-text">درخواست رد شده است</span>
            </div>
            <div class="reject-card-body">
              <img
                src="../src/images/user-profile-images/order-history/rejected-img.svg"
                alt="تصویر قاب گوشی"
                class="reject-product-image"
              />
              <div class="reject-product-details">
                <p class="reject-product-title">قاب گوشی گربه ای</p>
                <p class="reject-product-desc">
                  <img
                    src="../src/images/user-profile-images/order-history/info.svg"
                    alt="آیکن هشدار"
                    class="reject-icon-warning"
                  />
                  محصول با طرح اشتباه ارسال شده است
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="reject-back-button">
          <img
            src="../src/images/user-profile-images/order-history/arrow-left.svg"
            alt="آیکن بازگشت"
          />
        </div>
      </div>
    </div>
    <div class="rejected-item">
      <div class="reject-container">
        <div class="inner-container">
          <div class="reject-header">
            <span class="date">۳ شهریور ۱۴۰۲</span>
            <span class="tracking-code">کد پیگیری مرجوعی: ۳۵۴۵۳۴۵۲۱</span>
          </div>

          <div class="reject-card">
            <div class="reject-card-header">
              <img
                src="../src/images/user-profile-images/order-history/reject-icon.svg"
                alt="آیکن بستن"
                class="reject-icon-close"
              />
              <span class="rejected-text">درخواست رد شده است</span>
            </div>
            <div class="reject-card-body">
              <img
                src="../src/images/user-profile-images/order-history/rejected-img.svg"
                alt="تصویر قاب گوشی"
                class="reject-product-image"
              />
              <div class="reject-product-details">
                <p class="reject-product-title">قاب گوشی گربه ای</p>
                <p class="reject-product-desc">
                  <img
                    src="../src/images/user-profile-images/order-history/info.svg"
                    alt="آیکن هشدار"
                    class="reject-icon-warning"
                  />
                  محصول با طرح اشتباه ارسال شده است
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="reject-back-button">
          <img
            src="../src/images/user-profile-images/order-history/arrow-left.svg"
            alt="آیکن بازگشت"
          />
        </div>
      </div>
    </div>
    <div class="rejected-item">
      <div class="reject-container">
        <div class="inner-container">
          <div class="reject-header">
            <span class="date">۳ شهریور ۱۴۰۲</span>
            <span class="tracking-code">کد پیگیری مرجوعی: ۳۵۴۵۳۴۵۲۱</span>
          </div>

          <div class="reject-card">
            <div class="reject-card-header">
              <img
                src="../src/images/user-profile-images/order-history/reject-icon.svg"
                alt="آیکن بستن"
                class="reject-icon-close"
              />
              <span class="rejected-text">درخواست رد شده است</span>
            </div>
            <div class="reject-card-body">
              <img
                src="../src/images/user-profile-images/order-history/rejected-img.svg"
                alt="تصویر قاب گوشی"
                class="reject-product-image"
              />
              <div class="reject-product-details">
                <p class="reject-product-title">قاب گوشی گربه ای</p>
                <p class="reject-product-desc">
                  <img
                    src="../src/images/user-profile-images/order-history/info.svg"
                    alt="آیکن هشدار"
                    class="reject-icon-warning"
                  />
                  محصول با طرح اشتباه ارسال شده است
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="reject-back-button">
          <img
            src="../src/images/user-profile-images/order-history/arrow-left.svg"
            alt="آیکن بازگشت"
          />
        </div>
      </div>
    </div>
    <div class="rejected-item">
      <div class="reject-container">
        <div class="inner-container">
          <div class="reject-header">
            <span class="date">۳ شهریور ۱۴۰۲</span>
            <span class="tracking-code">کد پیگیری مرجوعی: ۳۵۴۵۳۴۵۲۱</span>
          </div>

          <div class="reject-card">
            <div class="reject-card-header">
              <img
                src="../src/images/user-profile-images/order-history/reject-icon.svg"
                alt="آیکن بستن"
                class="reject-icon-close"
              />
              <span class="rejected-text">درخواست رد شده است</span>
            </div>
            <div class="reject-card-body">
              <img
                src="../src/images/user-profile-images/order-history/rejected-img.svg"
                alt="تصویر قاب گوشی"
                class="reject-product-image"
              />
              <div class="reject-product-details">
                <p class="reject-product-title">قاب گوشی گربه ای</p>
                <p class="reject-product-desc">
                  <img
                    src="../src/images/user-profile-images/order-history/info.svg"
                    alt="آیکن هشدار"
                    class="reject-icon-warning"
                  />
                  محصول با طرح اشتباه ارسال شده است
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="reject-back-button">
          <img
            src="../src/images/user-profile-images/order-history/arrow-left.svg"
            alt="آیکن بازگشت"
          />
        </div>
      </div>
    </div>
    <div class="rejected-item">
      <div class="reject-container">
        <div class="inner-container">
          <div class="reject-header">
            <span class="date">۳ شهریور ۱۴۰۲</span>
            <span class="tracking-code">کد پیگیری مرجوعی: ۳۵۴۵۳۴۵۲۱</span>
          </div>

          <div class="reject-card">
            <div class="reject-card-header">
              <img
                src="../src/images/user-profile-images/order-history/reject-icon.svg"
                alt="آیکن بستن"
                class="reject-icon-close"
              />
              <span class="rejected-text">درخواست رد شده است</span>
            </div>
            <div class="reject-card-body">
              <img
                src="../src/images/user-profile-images/order-history/rejected-img.svg"
                alt="تصویر قاب گوشی"
                class="reject-product-image"
              />
              <div class="reject-product-details">
                <p class="reject-product-title">قاب گوشی گربه ای</p>
                <p class="reject-product-desc">
                  <img
                    src="../src/images/user-profile-images/order-history/info.svg"
                    alt="آیکن هشدار"
                    class="reject-icon-warning"
                  />
                  محصول با طرح اشتباه ارسال شده است
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="reject-back-button">
          <img
            src="../src/images/user-profile-images/order-history/arrow-left.svg"
            alt="آیکن بازگشت"
          />
        </div>
      </div>
    </div>
    <div class="rejected-item">
      <div class="reject-container">
        <div class="inner-container">
          <div class="reject-header">
            <span class="date">۳ شهریور ۱۴۰۲</span>
            <span class="tracking-code">کد پیگیری مرجوعی: ۳۵۴۵۳۴۵۲۱</span>
          </div>

          <div class="reject-card">
            <div class="reject-card-header">
              <img
                src="../src/images/user-profile-images/order-history/reject-icon.svg"
                alt="آیکن بستن"
                class="reject-icon-close"
              />
              <span class="rejected-text">درخواست رد شده است</span>
            </div>
            <div class="reject-card-body">
              <img
                src="../src/images/user-profile-images/order-history/rejected-img.svg"
                alt="تصویر قاب گوشی"
                class="reject-product-image"
              />
              <div class="reject-product-details">
                <p class="reject-product-title">قاب گوشی گربه ای</p>
                <p class="reject-product-desc">
                  <img
                    src="../src/images/user-profile-images/order-history/info.svg"
                    alt="آیکن هشدار"
                    class="reject-icon-warning"
                  />
                  محصول با طرح اشتباه ارسال شده است
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="reject-back-button">
          <img
            src="../src/images/user-profile-images/order-history/arrow-left.svg"
            alt="آیکن بازگشت"
          />
        </div>
      </div>
    </div>
      `;
    } else if (tabName === "لغو شده ۴") {
      tabCache[tabName] = `
        <div class="order-card">سفارش لغو شده ۱</div>
        <div class="order-card">سفارش لغو شده ۲</div>
      `;
    }
  }

  // جایگزینی محتوا
  container.innerHTML = tabCache[tabName];
}