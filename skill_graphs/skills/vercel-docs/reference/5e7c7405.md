##  [Complete examples](https://vercel.com/docs/botid/get-started#complete-examples)[](https://vercel.com/docs/botid/get-started#complete-examples)
###  [Next.js App Router example](https://vercel.com/docs/botid/get-started#next.js-app-router-example)[](https://vercel.com/docs/botid/get-started#next.js-app-router-example)
Client-side code for the BotID Next.js implementation:
app/checkout/page.tsx
```
'use client';

import { useState } from 'react';

export default function CheckoutPage() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  async function handleCheckout(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);

    try {
      const formData = new FormData(e.currentTarget);
      const response = await fetch('/api/checkout', {
        method: 'POST',
        body: JSON.stringify({
          product: formData.get('product'),
          quantity: formData.get('quantity'),
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Checkout failed');
      }

      const data = await response.json();
      setMessage('Checkout successful!');
    } catch (error) {
      setMessage('Checkout failed. Please try again.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleCheckout}>
      <input name="product" placeholder="Product ID" required />
      <input name="quantity" type="number" placeholder="Quantity" required />
      <button type="submit" disabled={loading}>
        {loading ? 'Processing...' : 'Checkout'}
      </button>
      {message && <p>{message}</p>}
    </form>
  );
}
```

Server-side code for the BotID Next.js implementation:
app/api/checkout/route.ts
```
import { checkBotId } from 'botid/server';
import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  // Check if the request is from a bot
  const verification = await checkBotId();

  if (verification.isBot) {
    return NextResponse.json(
      { error: 'Bot detected. Access denied.' },
      { status: 403 },
    );
  }

  // Process the legitimate checkout request
  const body = await request.json();

  // Your checkout logic here
  const order = await processCheckout(body);

  return NextResponse.json({
    success: true,
    orderId: order.id,
  });
}

async function processCheckout(data: any) {
  // Implement your checkout logic
  return { id: 'order-123' };
}
```

* * *
[ Previous BotID ](https://vercel.com/docs/botid)[ Next Handling Verified Bots ](https://vercel.com/docs/botid/verified-bots)
Was this helpful?
Send
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * SvelteKit
  * Nuxt
  * Other frameworks


On this page
  * [Step by step guide](https://vercel.com/docs/botid/get-started#step-by-step-guide)
  * [Install the package](https://vercel.com/docs/botid/get-started#install-the-package)
  * [Configure redirects](https://vercel.com/docs/botid/get-started#configure-redirects)
  * [Add client-side protection](https://vercel.com/docs/botid/get-started#add-client-side-protection)
  * [Perform BotID checks on the server](https://vercel.com/docs/botid/get-started#perform-botid-checks-on-the-server)
  * [Enable BotID deep analysis in Vercel (Recommended)](https://vercel.com/docs/botid/get-started#enable-botid-deep-analysis-in-vercel-recommended)
  * [Complete examples](https://vercel.com/docs/botid/get-started#complete-examples)
  * [Next.js App Router example](https://vercel.com/docs/botid/get-started#next.js-app-router-example)


Copy as MarkdownGive feedbackAsk AI about this page
